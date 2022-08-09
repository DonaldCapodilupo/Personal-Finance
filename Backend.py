import sqlite3, datetime, os


def programSetup(directories: tuple, databases: tuple, tables: tuple):
    for directory in directories:
        try:
            os.mkdir(directory)
            print("Database " + directory + " Created ")
        except FileExistsError:
            print(directory + " directory already exists")

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

def organize_Database(dataframe):
    account_Type_Nums = {
        "Current Asset": 0,
        "NonCurrent Asset": 1,
        "Current Liability": 2,
        "NonCurrent Liability": 3,
    }



    dataframe["Account Type Number"] = [account_Type_Nums[account] for account in
                                                dataframe["Account_Type"].values]

    organized_Dataframe = dataframe.sort_values(by=["Account Type Number", "Date"])
    organized_Dataframe = organized_Dataframe.drop(["Account Type Number"], axis=1)

    return organized_Dataframe



def create_Database_Row(database, table, tuple_Of_Values_To_Add):
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    tuple_To_Database_Syntax = "?, " * (len(tuple_Of_Values_To_Add) - 1)

    c.execute("INSERT INTO " + table + " VALUES (NULL," + tuple_To_Database_Syntax + "?)", tuple_Of_Values_To_Add)
    os.chdir('..')
    conn.commit()


def read_Database(database, table):
    import pandas as pd

    os.chdir("Databases")

    con = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * from " + table, con)
    con.close()

    clean_Data = organize_Database(df)

    os.chdir("..")
    return organize_Database(clean_Data)


def update_Database_Information(database, list_Of_New_Values, replace):


    current_Data = read_Database("Account_Balances.db", "Accounts")

    current_Data["Value"] = list_Of_New_Values
    os.chdir("Databases")

    conn = sqlite3.connect(database)

    if replace:
        current_Data.to_sql('Accounts', con=conn, if_exists='replace', index=False)
    else:
        current_Data = current_Data.drop(["ID"], axis=1)
        current_Data.to_sql('Accounts', con=conn, if_exists='append', index=False)

    os.chdir('..')
    conn.commit()


def delete_Database_Row(database, table, value_To_Remove):
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE FROM " + table + " where Account_Name = ?", [value_To_Remove])
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
        return end_Of_Year, str(datetime.date(ref.year, 6, 30)), today
    return end_Of_Year, str(datetime.date(ref.year, 9, 30)), today

def difference_Between_Percentage_Calculator(previous_Value: float, current_Value: float):
    import decimal
    try:
        return "{:,.2f}%".format(((current_Value - previous_Value) / previous_Value) * 100)
    except (decimal.DivisionByZero, decimal.InvalidOperation):
        return "0.00%"

def raw_Num_To_Currency(raw_Number: float):
    return "${:,.2f}".format(raw_Number)


def raw_Num_To_Percentage(raw_Number: float):
    return "{:,.2f}%".format(raw_Number)


def percentage_Or_Currency_To_Float(input_String: str):
    from re import sub
    from decimal import Decimal

    return Decimal(sub(r'[^\d.-]', '', input_String))


def create_Account_Balances_HTML_Table():
    import pandas as pd

    balances = {
       "EOY": {"Current Asset": 0.00,
               "NonCurrent Asset": 0.00,
               "Total Assets": 0.00,
               "Current Liability": 0.00,
               "NonCurrent Liability": 0.00,
               "Total Liabilities": 0.00,
               "Equity": 0.00},
       "EOQ": {"Current Asset": 0.00,
                   "NonCurrent Asset": 0.00,
                   "Total Assets": 0.00,
                   "Current Liability": 0.00,
                   "NonCurrent Liability": 0.00,
                   "Total Liabilities":0.00,
                   "Equity": 0.00},
       "Current": {"Current Asset": 0.00,
                   "NonCurrent Asset": 0.00,
                   "Total Assets": 0.00,
                   "Current Liability": 0.00,
                   "NonCurrent Liability": 0.00,
                   "Total Liabilities": 0.00,
                   "Equity": 0.00},
    }

    for row in read_Database("Backup_Balances.db", "Accounts").values:
        if row[1] == prior_Report_Dates()[0]:
            balances["EOY"][row[2]] += float(row[4])
        elif row[1] == prior_Report_Dates()[1]:
            balances["EOQ"][row[2]] += float(row[4])

    for row in read_Database("Account_Balances.db", "Accounts").values:
        balances["Current"][row[2]] += float(row[4])

    for key in balances:
        balances[key]["Total Assets"] = balances[key]["Current Asset"] + balances[key]["NonCurrent Asset"]
        balances[key]["Total Liabilities"] = balances[key]["Current Liability"] + balances[key]["NonCurrent Liability"]
        balances[key]["Equity"] = balances[key]["Total Assets"] - balances[key]["Total Liabilities"]

    for key in balances:
        for nested_Dict in balances[key]:
            balances[key][nested_Dict] = raw_Num_To_Currency(balances[key][nested_Dict])


    balances_Html = pd.DataFrame.from_dict(balances)
    balances_Html.to_html("templates/Account_Balances_Table.html", classes="table")

    return balances


def get_Account_Percentages():
    import pandas as pd

    balances = create_Account_Balances_HTML_Table()

    percentages = {"YTD $ Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""},
                   "YTD % Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""},
                   "QTD $ Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""},
                   "QTD % Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""}
                   }


    for table_Column in percentages:
        if "YTD %" in table_Column:
            for table_Row in percentages[table_Column]:

                percentages[table_Column][table_Row] = difference_Between_Percentage_Calculator(
                    percentage_Or_Currency_To_Float(balances["EOY"][table_Row]),
                    percentage_Or_Currency_To_Float(balances["Current"][table_Row])
                )
        elif "YTD $" in table_Column:
            for table_Row in percentages[table_Column]:
                percentages[table_Column][table_Row] = raw_Num_To_Currency (
                            percentage_Or_Currency_To_Float(balances["Current"][table_Row]) -
                            percentage_Or_Currency_To_Float(balances["EOY"][table_Row])
                            )
        elif "QTD %" in table_Column:
            for table_Row in percentages[table_Column]:

                percentages[table_Column][table_Row] = difference_Between_Percentage_Calculator(
                    percentage_Or_Currency_To_Float(balances["EOQ"][table_Row]),
                    percentage_Or_Currency_To_Float(balances["Current"][table_Row])
                )
        elif "QTD $" in table_Column:
            for table_Row in percentages[table_Column]:
                percentages[table_Column][table_Row] = raw_Num_To_Currency(
                    percentage_Or_Currency_To_Float(balances["Current"][table_Row]) -
                    percentage_Or_Currency_To_Float(balances["EOQ"][table_Row])
                )

    percentages_HTML = pd.DataFrame.from_dict(percentages)
    percentages_HTML.to_html("templates/Account_Percentages_Table.html", classes="table", index=False)

    return percentages


def create_Balance_Sheet_HTML():
    current_Balances_Database = read_Database("Account_Balances.db", "Accounts")

    # Rearange to current assets, noncurrent assets, total assets, etc.
    account_Type_Nums = {
        "Current Asset": 1,
        "NonCurrent Asset": 2,
        "Current Liability": 3,
        "NonCurrent Liability": 4,
    }
    current_Balances_Database["Account Type Number"] = [account_Type_Nums[account] for account in
                                                        current_Balances_Database["Account_Type"].values]
    current_Balances_Database = current_Balances_Database.sort_values(by=["Account Type Number"])

    # Add the "currenct balance in $" column
    current_Balances_Database["Current Value"] = [raw_Num_To_Currency(float(dollar_Amount)) for dollar_Amount in
                                                  current_Balances_Database["Value"].values]

    # drop unneeded columns
    balance_Sheet = current_Balances_Database.drop(['Account_Type', 'Value'], axis=1)

    # save file
    balance_Sheet.to_html("templates/Balance_Sheet.html", index=False, classes="table")

def get_Monthly_Account_Balances_Dict():
    import pandas as pd

    prior_Balances = read_Database("Backup_Balances.db", "Accounts")

    return_Dict = {}


    prior_Months = pd.date_range(prior_Report_Dates()[0], str(datetime.date.today()),
                  freq='MS').strftime("%Y-%b").tolist()


    #for row in



    for row in prior_Months:
        return_Dict[row[5:]] = ""

    daterange = pd.date_range(prior_Report_Dates()[0], str(datetime.date.today()), freq='1M').tolist()
    daterange = [d.strftime('%y-%b') for d in daterange]
    print(daterange)


    print(return_Dict)


