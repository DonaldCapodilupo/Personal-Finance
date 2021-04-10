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

balanceSheetSpecificToGeneral = {
                        "Cash":"Current Asset",
                       "Cash Equivalent_Bank_Accounts":"Current Asset",
                       "Short Term Investments":"Current Asset",
                       "Net Receivables":"Current Asset",
                        "Inventory":"Current_Asset",
                       "Other Current Assets":"Current Asset",
                       "Property Plant and Equipment":"NonCurrent Asset",
                       "Accumulated Depreciation":"NonCurrent Asset",
                        "Equity and Other Investments":"NonCurrent Asset",
                       "Goodwill":"NonCurrent Asset",
                       "Intangible Assets":"NonCurrent Asset",
                       "Other Long Term Assets":"NonCurrent Assets",
                       "Total Revenue":"Current Liability" ,
                       "Accounts Payable":"Current Liability" ,
                       "Taxes Payable":"Current Liability",
                       "Accrued Liabilities":"Current Liability",
                        "Other Current_Liabilities":"Current Liability",
                       "Long Term Debt":"NonCurrent Liability",
                       "Deferred Taxes Liabilities":"NonCurrent Liability",
                       "Deferred Revenues":"NonCurrent Liability",
                        "Other Long Term Liabilities":"NonCurrent Liability",

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

def add_Account_To_Database(term, primary_account_type, name,balance, specific_account_type):
    os.chdir('Databases')
    conn = sqlite3.connect(term + '_' + primary_account_type + '.db')
    c = conn.cursor()
    today = str(datetime.date.today())
    c.execute("INSERT INTO " + specific_account_type.replace(' ','_') + " VALUES (NULL, ?, ?, ?)",
              (today, name, balance))  # This line of code added a new row to the database.
    os.chdir('..')
    conn.commit()

def get_Specific_Account_Names_From_Database(primary_account_type):
    os.chdir('Databases')

    name_To_List = primary_account_type.split()

    returnDict = {}

    conn = sqlite3.connect(primary_account_type.replace(" ","_") + '.db')
    c = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]
    for table in completeBalanceSheet[name_To_List[1]][primary_account_type]:
        possibleChoices = c.execute("SELECT * FROM  "+table.replace(" ","_")).fetchall()
        try:
            returnDict[table] = [possibleChoices[0][2],possibleChoices[0][3]]
        except IndexError:
            returnDict[table] = []

    os.chdir('..')
    return returnDict


def get_All_Account_Names_From_Database():
    os.chdir('Databases')

    returnDict = {}

    for primary_Account_Type in completeBalanceSheet:
        returnDict[primary_Account_Type] = { }  #{Asset:{}}
        for generic_Account_Type in completeBalanceSheet[primary_Account_Type]:
            returnDict[primary_Account_Type][generic_Account_Type] = {}
            conn = sqlite3.connect(generic_Account_Type.replace(" ", "_") + '.db')
            c = conn.cursor()
            for table in completeBalanceSheet[primary_Account_Type][generic_Account_Type]:
                possibleChoices = c.execute("SELECT * FROM  " + table.replace(" ", "_" )).fetchall()
                try:
                    returnDict[primary_Account_Type][generic_Account_Type][table] = [possibleChoices[0][2], possibleChoices[0][3]]
                except IndexError:
                    returnDict[primary_Account_Type][generic_Account_Type][table] = []

    os.chdir('..')
    return returnDict



def remove_Account_From_Database(list_of_Items):
    os.chdir('Databases')

    proper_Tuple = tuple(list_of_Items.replace('\\',"").replace('[',"").replace('\'',"").replace('(',"").replace(')',"").split(', '))

    conn = sqlite3.connect(balanceSheetSpecificToGeneral[proper_Tuple[0]].replace(" ", "_") + '.db')
    c = conn.cursor()
    c.execute('DELETE FROM ' + proper_Tuple[0].replace(" ", "_") + ' WHERE Description = ?',
              (proper_Tuple[1].replace(" ", "_"),))
    os.chdir('..')
    conn.commit()

    
