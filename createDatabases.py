import sqlite3
def setupTable(c,i):
    for s in i:
        try:
            c.execute("CREATE TABLE  " + s + "(ID INTEGER PRIMARY KEY, "
                                             "Date TEXT, "
                                             "Description TEXT,"
                                             "Value TEXT)")
            print("Creating the Database table:  " + s)
        except sqlite3.OperationalError:
            print("The table  " + s + " is already present and does not need to be created.")

def databaseSetup():
    dataBaseNames = ["Current_Assets", "NonCurrent_Assets", "Current_Liabilities", "NonCurrent_Liabilities"]
    from Dictionaries.PFinanceDicts import completeBalanceSheet
    for nameOfDatabase in dataBaseNames:

        conn = sqlite3.connect(nameOfDatabase+'.db')
        c = conn.cursor()

        if nameOfDatabase == dataBaseNames[0]:
            setupTable(c, completeBalanceSheet["Assets"]["Current Assets"])
        elif nameOfDatabase == dataBaseNames[1]:
            setupTable(c, completeBalanceSheet["Assets"]["NonCurrent Assets"])
        elif nameOfDatabase == dataBaseNames[2]:
            setupTable(c, completeBalanceSheet["Liabilities"]["Current Liabilities"])
        elif nameOfDatabase == dataBaseNames[3]:
            setupTable(c, completeBalanceSheet["Liabilities"]["NonCurrent Liabilities"])

    print("The database is set up properly.\n")