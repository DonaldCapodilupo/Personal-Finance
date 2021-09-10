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
    date_Current_Balances =""

    current_Balances = read_Database("Account_Balances.db", "Accounts")
    for row in current_Balances.values:
        date_Current_Balances = row[1]
        break


    ref = datetime.date.today()
    if ref.month < 4:
        return end_Of_Year, str(datetime.date(ref.year - 1, 12, 31))
    elif ref.month < 7:
        return end_Of_Year, str(datetime.date(ref.year, 3, 31))
    elif ref.month < 10:
        return end_Of_Year, str( datetime.date(ref.year, 6, 30))
    return end_Of_Year, str(datetime.date(ref.year, 9, 30))



def prior_Account_Balances():

    balances = {
        "Current":{"Equity": 0},
        "EOQ": {"Equity": 0},
        "EOY": {"Equity": 0},

    }

    account_Types = ("Current Asset", "NonCurrent Asset", "Current Liability", "NonCurrent Liability")

    previous_Balances = read_Database("Backup_Balances.db", "Accounts")
    current_Balances = read_Database("Account_Balances.db", "Accounts")
    the_Balances = (current_Balances, previous_Balances)

    tuple_Of_Balance_Dataframes = (previous_Balances,current_Balances)

    list_Of_Previous_Date_Dataframes = [date for dates, date in previous_Balances.groupby('Date')]

    for df in list_Of_Previous_Date_Dataframes:
        if df["Date"].values[0] == prior_Report_Dates()[1]:
            balance_Sheet = df.groupby('Account_Type')['Value'].sum()
            for account in account_Types:
                try:
                    balances["EOQ"][account] = int(balance_Sheet[account])
                    if "Asset" in account:
                        balances["EOQ"]["Equity"] += int(balance_Sheet[account])
                    else:
                        balances["EOQ"]["Equity"] -= int(balance_Sheet[account])
                except KeyError:
                    print("Wow, are there really no occurrences of " + account + " in the database?")
                    balances["EOQ"][account] = 0
        elif df["Date"].values[0] == prior_Report_Dates()[0]:
            balance_Sheet = df.groupby('Account_Type')['Value'].sum()
            for account in account_Types:
                try:
                    balances["EOY"][account] = int(balance_Sheet[account])
                    if "Asset" in account:
                        balances["EOY"]["Equity"] += int(balance_Sheet[account])
                    else:
                        balances["EOY"]["Equity"] -= int(balance_Sheet[account])
                except KeyError:
                    print("Wow, are there really no occurrences of " + account + " in the database?")
                    balances["EOY"][account] = 0


    #Current
    current_Account_Balances = current_Balances.groupby('Account_Type')['Value'].sum()
    for account in account_Types:
        try:
            balances["Current"][account] = current_Account_Balances[account]
            if "Asset" in account:
                balances["Current"]["Equity"] += int(current_Account_Balances[account])
            else:
                balances["Current"]["Equity"] -= int(current_Account_Balances[account])
        except KeyError:
            print("Wow, are there really no occurrences of " + account + " in the database?")
            balances["Current"][account] = 0

    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(pd.DataFrame.from_dict(balances))

    return balances


def get_Account_Percentages():
    import pandas as pd
    balances_Dict = prior_Account_Balances()
    current_Balances = read_Database("Account_Balances.db","Accounts")

    for key in balances_Dict.keys():


        balances_Items = balances_Dict[key].items()
        balances_List = list(balances_Items)

        df = pd.DataFrame(balances_List)
        print(df)



print()


#get_Account_Percentages()