import sqlite3, datetime, os

completeBalanceSheet = {"Asset":{"Current Asset":{"Cash": {},"Cash Equivalent Bank Accounts":{}, "Short Term Investments":{},
                                                    "Net Receivables":{},"Inventory":{}, "Other Current Assets":{}},
                                  "NonCurrent Asset":{"Property Plant and Equipment":{}, "Accumulated Depreciation":{},
                                                        "Equity and Other Investments":{},"Goodwill":{}, "Intangible Assets":{},
                                                        "Other Long Term Assets":{}}
                                  },
                        "Liability":{"Current Liability":{"Total Revenue":{}, "Accounts Payable":{}, "Taxes Payable":{},
                                                              "Accrued Liabilities":{}, "Deferred Revenues":{},
                                                              "Other Current Liabilities":{}},
                                       "NonCurrent Liability":{"Long Term Debt":{}, "Deferred Taxes Liabilities":{},
                                                                  "Deferred Revenues":{},"Other Long Term Liabilities":{}}
                                     },
                        "Equity":{"True Equity":["Common Stock", "Retained Earnings", "Accumulated Other Comprehensive Income"]
                                  },
                        "Income":{"Current Income":["Main Paycheck","Investment Income","Business Income","Gift Income"]
                                  },
                        "Expenses":{"Current Expense":["Rent Expense","Insurance Expense","Gas Expense","Food Expense",
                                                "Education Expense", "Alcohol Expense", "Misc Expense"]
                                    }
                        }


def programSetup():
    import os
    import sqlite3
    try:
        os.mkdir("Databases")
        print("Database Directory Created ")
    except FileExistsError:
        print("Database directory already exists")

    os.chdir("Databases")

    for primary_Account_Type in completeBalanceSheet.keys():
        for database_Name in completeBalanceSheet[primary_Account_Type]:
            conn = sqlite3.connect(database_Name.replace(" ","_") + '.db')
            c = conn.cursor()
            for table_Name in completeBalanceSheet[primary_Account_Type][database_Name]:
                try:
                    c.execute("CREATE TABLE  " + table_Name.replace(" ", "_") + "(ID INTEGER PRIMARY KEY, "
                                                          "Date TEXT, "
                                                          "Description TEXT,"
                                                          "Value TEXT)")
                except sqlite3.OperationalError:
                    print(table_Name + " already exists.")
    os.chdir('..')

#{'Asset': {'Current Asset': {'Cash': {'Wallet Cash': '1 mill', 'Spare Change': '0.35'}, 'Cash Equivalent Bank Accounts': {'Bank Acct': '100.00', 'Chase Bank': '1000'} } } }
def get_Current_Balance_Information_From_Database():
    os.chdir('Databases')
    import copy

    returnDict = copy.deepcopy(dict(completeBalanceSheet))

    for primary_Account_Type in returnDict:
        for account_Term in returnDict[primary_Account_Type]:
            conn = sqlite3.connect(account_Term.replace(" ", "_") + '.db')
            c = conn.cursor()
            for specific_Account_Type in returnDict[primary_Account_Type][account_Term]:
                for row in c.execute("SELECT * FROM  " + specific_Account_Type.replace(" ", "_" ) + " ORDER BY Date"):
                    returnDict[primary_Account_Type][account_Term][specific_Account_Type][row[2]] = row[3]
    os.chdir('..')
    return returnDict


#{'Asset': {'Current Asset': {'Cash': {'Wallet Cash': '1 mill', 'Spare Change': '0.35'}, 'Cash Equivalent Bank Accounts': {'Bank Acct': '100.00', 'Chase Bank': '1000'} } } }
def update_Account_Balances(dict_Of_Values):
    os.chdir('Databases')

    today = str(datetime.date.today())

    for primary_Account_Type in dict_Of_Values.keys():
        if primary_Account_Type in ['Asset', 'Liability']:
            for account_Term in dict_Of_Values[primary_Account_Type]:
                conn = sqlite3.connect(account_Term.replace(" ", "_") + '.db')
                for table_To_Update, value_List in dict_Of_Values[primary_Account_Type][account_Term].items():
                    for name, balance in value_List.items():
                        c = conn.cursor()
                        c.execute("INSERT INTO "+ table_To_Update.replace(' ','_') + " VALUES (NULL, ?, ?, ?)", (today, name, balance))
                        conn.commit()

    os.chdir('..')


def add_Account_To_Database(term, primary_account_type, name,balance, specific_account_type):
    os.chdir('Databases')
    conn = sqlite3.connect(term + '_' + primary_account_type + '.db')
    c = conn.cursor()
    today = str(datetime.date.today())
    c.execute("INSERT INTO " + specific_account_type.replace(' ','_') + " VALUES (NULL, ?, ?, ?)",
              (today, name, balance))  # This line of code added a new row to the database.
    os.chdir('..')
    conn.commit()


def remove_Account_From_Database(list_of_Items):
    os.chdir('Databases')

    proper_Tuple = tuple(list_of_Items.replace('\\',"").replace('[',"").replace('\'',"").replace('(',"").replace(')',"").split(', '))

    conn = sqlite3.connect(proper_Tuple[1].replace(" ", "_") + '.db')
    c = conn.cursor()
    c.execute('DELETE FROM ' + proper_Tuple[2].replace(" ", "_") + ' WHERE Description = ?',
              (proper_Tuple[3],))
    os.chdir('..')
    conn.commit()

    
