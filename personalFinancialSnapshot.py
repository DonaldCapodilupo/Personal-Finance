import os
from Dictionaries.PFinanceDicts import *
import sqlite3


#from Finance_Data_Visualization import *
programDirectory = os.getcwd()
csvHistoryDirectory = (programDirectory +"\Historical Data")
databaseDirectory = (programDirectory + "\Databases")

#Make sure that all directories are present.
#Make sure that the Database is present and set up with all of the apopriate tables.
def initialSetup():  #This will ensure that all required files and directories are present before continuing.


    print("Initializing setup.\n")

    # Create directories
    neededDirectories = ['Historical Data', 'Databases']
    for i in neededDirectories:
        try:
            # Create target Directory
            os.mkdir(i)
            print("Directory " +i+ " Created ")
        except FileExistsError:
            print("Directory "+ i+ " already exists")
    print("All directories are present.\n")

    os.chdir(databaseDirectory)
    from createDatabases import databaseSetup
    databaseSetup()

def sumDbTable(total, c, tables, asset=True):
    for table in tables:
        for row in [c.execute('SELECT * FROM  ' + table).fetchall()]:
            for i in row:
                if asset:
                    total["Assets"].append(float(i[3]))
                else:
                    total["Liabilities"].append(float(i[3]))

def displayTotals():
    import sqlite3
    os.chdir(databaseDirectory)

    total = {"Assets":[],"Liabilities":[], "Equity":[]}

    #Creates a list of ['Current Assets', 'NonCurrent Assets', 'Current Liabilities', 'NonCurrent Liabilities']
    allAccountTypes = list(completeBalanceSheet["Assets"].keys()) + list(completeBalanceSheet["Liabilities"].keys())

    for db in allAccountTypes:
        databaseChoice = (db.replace(" ","_") + ".db") #Converts "Current Assets" into "Current_Assets.db"
        conn = sqlite3.connect(databaseChoice)
        c = conn.cursor()
        #conn.row_factory = lambda cursor, row: row[0]
        #print("What " + accountType + " would you like to remove from your Balance Sheet?")
        if databaseChoice == "Current_Assets.db":
            print("Gathering Current Asset totals.\n")
            sumDbTable(total,c,completeBalanceSheet["Assets"]["Current Assets"])
        elif databaseChoice == "NonCurrent_Assets.db":
            print("Gathering NonCurrent Asset totals.\n")
            sumDbTable(total, c, completeBalanceSheet["Assets"]["NonCurrent Assets"])
        elif databaseChoice == "Current_Liabilities.db":
            print("Gathering Current Liability totals.\n")
            sumDbTable(total, c, completeBalanceSheet["Liabilities"]["Current Liabilities"],False)
        elif databaseChoice == "NonCurrent_Liabilities.db":
            print("Gathering NonCurrent Liability totals.\n")
            sumDbTable(total, c, completeBalanceSheet["Liabilities"]["NonCurrent Liabilities"],False)
    print("***Totals Gathered***")

    assetsTotal = sum(total["Assets"])
    liabilitiesTotal = sum(total["Liabilities"])
    equity = (assetsTotal - liabilitiesTotal)

    print("Assets total: $"+str(assetsTotal)+"\n")
    print("Liabilities total: $" + str(liabilitiesTotal)+"\n")
    print("Equity total: $" + str(equity)+"\n")

    print("Hit enter when ready to return to the main menu")
    input()
    mainDirectory()




#Iterates through Assets and Liabilities columns, updating the "Value" column with user input.
def getSQLTableInfo(table, conn, c, row):
    from AccountClasses import balance_Sheet_Item
    print("What is the current balance of " + str(row[2]) + "?")
    accountBalanceLoop = input(">")
    account = balance_Sheet_Item((str(row[0])), (str(row[2])), accountBalanceLoop)
    c.execute("UPDATE " + table + " SET Value =" + account.accountBalance + " WHERE ID = " + account.accountID)
    conn.commit()

def iterSQLiteTable(db, appropriateTableList):
    for table in appropriateTableList: #Iterate through each table in the db. The list comes from completeBalanceSheet[]
        conn = sqlite3.connect(db)  # create a connection the database/create it if it doesn't exist.
        c = conn.cursor()  # no clue what this does specifically.
        for row in c.execute('SELECT * FROM ' + table + ' ORDER BY ID').fetchall():
            getSQLTableInfo(table,conn,c,row)

def updateDatabaseColumns():
    from Dictionaries.PFinanceDicts import completeBalanceSheet
    os.chdir(databaseDirectory)
    databasesToUpdate = ["Current_Assets.db","Current_Liabilities.db"]
    #Connect to the database to get asset names.
    for db in databasesToUpdate:
        if db == "Current_Assets.db":
            iterSQLiteTable(db, completeBalanceSheet["Assets"]["Current Assets"])
        elif db == "Current_Liabilities.db":
            iterSQLiteTable(db, completeBalanceSheet["Liabilities"]["Current Liabilities"])

    print("\nBalances Updated")
    mainDirectory()

def updateCSV(lineItem):
    import csv, datetime
    today = datetime.date.today()  # Records the date that the account balances were updated.
    os.chdir(csvHistoryDirectory)
    with open('Historical Data.csv', 'a', newline='') as csvfile:
        outputWriter = csv.writer(csvfile)
        row = [today, lineItem.accountNickName, lineItem.accountBalance]
        outputWriter.writerow(row)

def createCSVObject(row):
    from AccountClasses import balance_Sheet_Item
    lineItem = balance_Sheet_Item("Null", row[2], row[3])
    updateCSV(lineItem)

def getCSVData(db, appropriateTableList):
    os.chdir(databaseDirectory)
    conn = sqlite3.connect(db)  # create a connection the database/create it if it doesn't exist.
    c = conn.cursor()  # no clue what this does specifically.
    for table in appropriateTableList:
        # Append both the "Account Name" and  "'Current' Account Balance" to separate lists.
        for row in c.execute('SELECT * FROM ' + table + ' ORDER BY Description'):
            createCSVObject(row)

#Pulls all of the current Assets and Liabilities table values and appends them to a CSV.
def updateHistoricalCSV():
    print("Backing up current account balances to "+csvHistoryDirectory)
    #Connect to the database to get asset/liability names.
    dataBaseNames = ["Current_Assets.db", "NonCurrent_Assets.db", "Current_Liabilities.db", "NonCurrent_Liabilities.db"]


    for db in dataBaseNames:
        if db == 'Current_Assets.db':
            getCSVData(db, completeBalanceSheet["Assets"]["Current Assets"])
            print("Current Assets have been backed up.")
        elif db == 'NonCurrent_Assets.db':
            getCSVData(db, completeBalanceSheet["Assets"]["NonCurrent Assets"])
            print("NonCurrent Assets have been backed up.")
        elif db == 'Current_Liabilities.db':
            getCSVData(db, completeBalanceSheet["Liabilities"]["Current Liabilities"])
            print("Current Liabilities have been backed up.")
        elif db == 'NonCurrent_Liabilities.db':
            getCSVData(db, completeBalanceSheet["Liabilities"]["NonCurrent Liabilities"])
            print("NonCurrent Liabilities have been backed up.")

    print("All accounts have been backed up.\n")

#Displays all of the current rows in a table, allows the user to select one and remove it from the table.
def removeDatabaseRow(accountType):
    import sqlite3
    from Dictionaries.PFinanceDicts import balanceSheetSpecificToGeneral
    os.chdir(databaseDirectory)
    databaseChoice = (balanceSheetSpecificToGeneral[accountType] + ".db")
    conn = sqlite3.connect(databaseChoice)
    c = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]

    print("What " + accountType + " would you like to remove from your Balance Sheet?")

    #Produces a numerical list based off of the desired sqlite column
    possibleChoices = [c.execute('SELECT * FROM '+accountType).fetchall()]
    acceptableChoices = []
    for i in possibleChoices:
        for s in i:
            acceptableChoices.append(s[2])
    acceptableChoices.append("Exit")        #Would like to shrink into one line. (you can't append a list to a list)

    #Prompts the user to select the item to remove from the database.
    userChoice = listDisplay(acceptableChoices)

    #remove data
    c.execute('DELETE FROM '+accountType+' WHERE Description = ?',(userChoice,)) #userChoice needs to be a tuple or it will throw a "no such column as userChoice"
    conn.commit()

    #Converts the string back so the confirmation sentences is grammatically correct.
    print(userChoice+" has been deleted from "+accountType)
    mainDirectory()

#Allows the user to add new rows to a table in the Database.
def addDatabaseRow(accountType):
    import sqlite3, datetime
    from Dictionaries.PFinanceDicts import balanceSheetSpecificToGeneral
    from AccountClasses import balance_Sheet_Item
    os.chdir(databaseDirectory)
    databaseChoice = (balanceSheetSpecificToGeneral[accountType] +".db")
    conn = sqlite3.connect(databaseChoice)  # create a connection the database/create it if it doesn't exist.
    c = conn.cursor()  # no clue what this does specifically.
    #Ensure database name and proper grammar don't interrupt each other.
    #pluralDict = {"Asset": "Assets", "Liability": "Liabilities", "Income": "Incomes", "Expense": "Expenses"}
    #accountTypePlural = pluralDict[accountType]  # Returns the plural version of "accountType" ex. Asset -> Assets

    #Get user input and format it to be added to the SQLite database.
    today = str(datetime.date.today())#Each record will have the date recorded.

    print("Please give a description for the " + accountType + ".")
    assetDescription = input(">")
    print("What is the current value of the " + accountType + ".")
    assetAccountBalance = input(">")

    newRow = balance_Sheet_Item("No ID needed",assetDescription, assetAccountBalance )

    #Append the data to the proper table in the database. Confirm for the user. Return to main menu.
    c.execute("INSERT INTO " + accountType + " VALUES (NULL, ?, ?, ?)",
              (today, newRow.accountNickName, newRow.accountBalance))  # This line of code added a new row to the database.
    conn.commit()
    print(accountType + " has been added.\n")
    mainDirectory()

#Takes a list and converts it into a form that users can select a numerical option. Return value is a string.
#EX. ( '1)Assets' returns 'Assets
def listDisplay(acceptableChoices):

    print("Which option would you like to choose")
    s = 1   #This is the counter
    for i in acceptableChoices: #Loop through the menu options
        print(str(s) + ") " +i) #Display all of the items in the list as a menu
        s += 1
    userChoice = int(input(">")) #Prompt the user to enter a number
    # Reruns the prompt if the user enters a number that is to big
    while userChoice > len(acceptableChoices):
        print("Invalid data. Please enter a valid number")
        print()
        print("Which option would you like to choose")
        s = 1  # This is the counter
        for i in acceptableChoices:  # Loop through the menu options
            print(str(s) + ") " + i)  # Display all of the items in the list as a menu
            s += 1
        userChoice = int(input(">"))
    #Closes the program if the user selects "Exit"
    #At some point I would like it to step back one function
    if userChoice == (s-1) and acceptableChoices[-1] == "Exit":
        print("Exiting")
        exit()
    #Converts the users numerical entry into the string version of the option selected.
    userChoiceFINAL = acceptableChoices[(int(userChoice)-1)]
    #Return the variable
    return userChoiceFINAL

#Prompts the user to decide if they are manipulating an Asset, a Liability, Income or Expense
def decisionAccountType():
    from getAccountType import main
    decision = main()
    return decision

#Firing order of all other functions.
def mainDirectory():
    os.chdir(programDirectory)

    acceptableChoices = ["Update Account Balances","Add a Record","Remove a Record","View Current Balances","Exit"]        #Need to add "See most upd to date financial data"

    userChoice = listDisplay(acceptableChoices)



    if userChoice == acceptableChoices[0]:              #Update Account Balances
        updateHistoricalCSV()
        updateDatabaseColumns()
    elif userChoice == acceptableChoices[1]:            #Add An Account
        addDatabaseRow(decisionAccountType())        #Decide if the user is adding an asset or a liability Add the item to the appropriate database.
    elif userChoice == acceptableChoices[2]:            #Remove An Account
        removeDatabaseRow(decisionAccountType())
    elif userChoice == acceptableChoices[3]:  # Remove An Account
        displayTotals()
    elif userChoice == acceptableChoices[-1]:
        exit()

                                                        #Exit is handled in the listDisplay function.

if __name__ == "__main__":
    print("Hell, Welcome to the Personal Finance Software V0.30")
    print("At this time we assume you are Donald Capodilupo\n")
    initialSetup()
    mainDirectory()