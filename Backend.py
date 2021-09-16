import sqlite3, datetime, os


def programSetup(directories:tuple, databases:tuple,tables:tuple):
    for directory in directories:
        try:
            os.mkdir(directory)
            print("Database " + directory + " Created ")
        except FileExistsError:
            print(directory+" directory already exists")

    os.chdir("Databases")

    for database in databases:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        for table_Name in tables:
            try:
                c.execute("CREATE TABLE  " + table_Name + "(ID INTEGER PRIMARY KEY, "
                                                                            "Date TEXT, "
                                                                            "Account_Type TEXT, "
                                                                            "Account_Name TEXT, "
                                                                            "Value TEXT)")
            except sqlite3.OperationalError:
                print(table_Name + " already exists.")

    os.chdir('..')

def create_Database_Row(database, table, tuple_Of_Values_To_Add):
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    tuple_To_Database_Syntax = "?, " * (len(tuple_Of_Values_To_Add)-1)

    c.execute("INSERT INTO "+table+" VALUES (NULL,"+tuple_To_Database_Syntax +"?)",tuple_Of_Values_To_Add)
    os.chdir('..')
    conn.commit()

def read_Database(database, table):
    import pandas as pd

    os.chdir("Databases")

    con = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * from "+ table, con)
    con.close()

    os.chdir("..")
    return df

def update_Database_Information(database, dataframe, replace):
    os.chdir("Databases")

    conn = sqlite3.connect(database)

    if replace:
        dataframe.to_sql('Accounts', con=conn, if_exists='replace', index=False)
    else:
        dataframe.to_sql('Accounts', con=conn, if_exists='append', index_label='id')

    os.chdir('..')
    conn.commit()

def delete_Database_Row(database, table, value_To_Remove):
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE FROM "+ table +" where Account_Name = ?", [value_To_Remove])
    os.chdir('..')
    conn.commit()


def prior_Report_Dates():
    today = str(datetime.date.today())
    end_Of_Year = today[0:2] + str(int(today[2:4]) - 1) + '-12-31'


    current_Balances = read_Database("Account_Balances.db", "Accounts")
    for row in current_Balances.values:
        date_Current_Balances = row[1]
        break


    ref = datetime.date.today()
    if ref.month < 4:
        return end_Of_Year, str(datetime.date(ref.year - 1, 12, 31)), today
    elif ref.month < 7:
        return end_Of_Year, str(datetime.date(ref.year, 3, 31)), today
    elif ref.month < 10:
        return end_Of_Year, str( datetime.date(ref.year, 6, 30)), today
    return end_Of_Year, str(datetime.date(ref.year, 9, 30)), today



def create_Account_Balances_HTML_Table():
    import pandas as pd



    balances = {
        "Current": {"Current Asset": 0,
                    "NonCurrent Asset": 0,
                    "Total Assets": 0,
                    "Current Liability": 0,
                    "NonCurrent Liability": 0,
                    "Total Liabilities":0,
                    "Equity": 0},
        "EOQ": {"Current Asset": 0,
                    "NonCurrent Asset": 0,
                    "Total Assets": 0,
                    "Current Liability": 0,
                    "NonCurrent Liability": 0,
                    "Total Liabilities":0,
                    "Equity": 0},
        "EOY": {"Current Asset": 0,
                    "NonCurrent Asset": 0,
                    "Total Assets": 0,
                    "Current Liability": 0,
                    "NonCurrent Liability": 0,
                    "Total Liabilities":0,
                    "Equity": 0},

    }



    #[raw_Num_To_Currency(float(dollar_Amount)) for dollar_Amount in current_Balances_Database["Value"].values]

    for row in read_Database("Backup_Balances.db", "Accounts").values:
        print(prior_Report_Dates())
        #EOY
        if row[1] == prior_Report_Dates()[0]:
            print(prior_Report_Dates()[0])
            balances["EOY"][row[2]] += float(row[4])
        elif row[1] == prior_Report_Dates()[1]:
            balances["EOQ"][row[2]] += float(row[4])

    for row in read_Database("Account_Balances.db", "Accounts").values:
        balances["Current"][row[2]] += float(row[4])

    #Totals
    for key in balances:
        balances[key]["Total Assets"] = balances[key]["Current Asset"] + balances[key]["NonCurrent Asset"]
        balances[key]["Total Liabilities"] = balances[key]["Current Liability"] + balances[key]["NonCurrent Liability"]
        balances[key]["Equity"] = balances[key]["Total Assets"] - balances[key]["Total Liabilities"]


    for key in balances:
        for cat in balances[key]:
            balances[key][cat] = raw_Num_To_Currency(float(balances[key][cat]))




    balances = pd.DataFrame.from_dict(balances)
    balances.to_html("templates/Account_Balances_Table.html", classes="table")



def get_Account_Percentages():
    import pandas as pd
    balances_Dict = prior_Account_Balances()
    current_Balances = read_Database("Account_Balances.db","Accounts")

    for key in balances_Dict.keys():


        balances_Items = balances_Dict[key].items()
        balances_List = list(balances_Items)

        df = pd.DataFrame(balances_List)
        print(df)

def raw_Num_To_Currency(raw_Number:float):
    return "${:,.2f}".format(raw_Number)

def raw_Num_To_Percentage(raw_Number:float):
    return "%{:,.2f}".format(raw_Number)

def create_Balance_Sheet_HTML():
    current_Balances_Database = read_Database("Account_Balances.db", "Accounts")



    #Rearange to current assets, noncurrent assets, total assets, etc.
    account_Type_Nums = {
        "Current Asset":1,
        "NonCurrent Asset": 2,
        "Current Liability": 3,
        "NonCurrent Liability": 4,
    }
    current_Balances_Database["Account Type Number"] = [account_Type_Nums[account] for account in current_Balances_Database["Account_Type"].values]
    current_Balances_Database = current_Balances_Database.sort_values(by=["Account Type Number"])



    #Add the "currenct balance in $" column
    current_Balances_Database["Current Value"] = [raw_Num_To_Currency(float(dollar_Amount)) for dollar_Amount in current_Balances_Database["Value"].values]


    #drop unneeded columns
    balance_Sheet = current_Balances_Database.drop(['ID', 'Account_Type', 'Value', 'Account Type Number'], axis=1)

    #save file
    balance_Sheet.to_html("templates/Balance_Sheet.html", index=False, classes="table")

def create_Current_Balances_Table_HTML():
    import pandas as pd
    balances = {
        "Current": {"Current Asset": 0,
                    "NonCurrent Asset": 0,
                    "Current Liability": 0,
                    "NonCurrent Liability": 0,
                    "Equity": 0},
        }

    # [raw_Num_To_Currency(float(dollar_Amount)) for dollar_Amount in current_Balances_Database["Value"].values]

    for row in read_Database("Account_Balances.db", "Accounts").values:
        balances["Current"][row[2]] += float(row[4])


    current_Balances_Table = pd.DataFrame.from_dict(balances)
    current_Balances_Table.to_html("templates/Current_Balances.html", classes="table")









