import sqlite3, datetime, os

completeBalanceSheet = {"Asset":{"Current Asset":["Cash","Cash Equivalent Bank Accounts", "Short Term Investments",
                                                    "Net Receivables","Inventory", "Other Current Assets"],
                                  "NonCurrent Asset":["Property Plant and Equipment", "Accumulated Depreciation",
                                                        "Equity and Other Investments","Goodwill", "Intangible Assets",
                                                        "Other Long Term Assets"]
                                  },
                        "Liability":{"Current Liability":["Total Revenue", "Accounts Payable", "Taxes Payable",
                                                              "Accrued Liabilities", "Deferred Revenues",
                                                              "Other Current Liabilities"],
                                       "NonCurrent Liability":["Long Term Debt", "Deferred Taxes Liabilities",
                                                                  "Deferred Revenues","Other Long Term Liabilities"]
                                     },
                        "Equity":{"True Equity":["Common Stock", "Retained Earnings", "Accumulated Other Comprehensive Income"]
                                  },
                        "Income":{"Current Income":["Main Paycheck","Investment Income","Business Income","Gift Income"]
                                  },
                        "Expenses":{"Current Expense":["Rent Expense","Insurance Expense","Gas Expense","Food Expense",
                                                "Education Expense", "Alcohol Expense", "Misc Expense"]
                                    }
                        }


def databaseSetup():
    import os
    import sqlite3
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




def add_Account_To_Database(term, primary_account_type, name,balance, specific_account_type):
    os.chdir('Databases')
    conn = sqlite3.connect(term + '_' + primary_account_type + 's.db')
    c = conn.cursor()
    today = str(datetime.date.today())
    c.execute("INSERT INTO " + specific_account_type.replace(' ','_') + " VALUES (NULL, ?, ?, ?)",
              (today, name, balance))  # This line of code added a new row to the database.
    os.chdir('..')
    conn.commit()

def get_Account_Names_From_Database(primary_account_type,terms):
    os.chdir('Databases')

    returnDict = {}
    for term in terms:
        conn = sqlite3.connect(term + '_' + primary_account_type + 's.db')
        c = conn.cursor()
        conn.row_factory = lambda cursor, row: row[0]
        for table in completeBalanceSheet[primary_account_type + 's'][term + '_' + primary_account_type + 's']:
            try:
                possibleChoices = c.execute("SELECT * FROM  "+table).fetchall()
                returnDict[table] = possibleChoices
            except:
                pass




    return returnDict

def remove_Account_From_Database(term, primary_account_type, name, specific_account_type):
    os.chdir('Databases')
    conn = sqlite3.connect(term + '_' + primary_account_type + 's.db')
    c = conn.cursor()
    c.execute('DELETE FROM ' + specific_account_type + ' WHERE Description = ?',
              (name,))
    os.chdir('..')
    conn.commit()

    
