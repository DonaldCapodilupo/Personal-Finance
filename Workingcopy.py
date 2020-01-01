

def showSQLcolumn(accountType):
    possibleChoices = [c.execute('SELECT * FROM ' + accountType).fetchall()]
    acceptableChoices = []
    for i in possibleChoices:
        for s in i:
            acceptableChoices.append(s[2])
    acceptableChoices.append("Exit")  # Would like to shrink into one line. (you can't append a list to a list)

    #Prompts the user to select the item to remove from the database.
    userChoice = listDisplay(acceptableChoices)
    return userChoice


def updateAccounts():
    import sqlite3, os, csv, datetime
    #os.chdir("/home/doncapodilupo/.PyCharmCE2019.2/config/scratches/Personal Finance/Databases/")  # Change directory so databases are localized
    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Databases")

    conn = sqlite3.connect('Finances.db')  # create a connection the database/create it if it doesn't exist.
    c = conn.cursor()  # no clue what this does specifically.

    newBalances = {"Assets":[],"Liabilities":[]}


    for row in c.execute('SELECT * FROM Assets ORDER BY Description'):
        print("What is the current balance of "+ str(row[2]+"?"))
        accountBalanceLoop = input(">")
        newBalances["Assets"].append(accountBalanceLoop)
    for row in c.execute('SELECT * FROM Liabilities ORDER BY Descriprion'):
        print("What is the current balance of "+ str(row[2]+"?"))
        accountBalanceLoop = input(">")
        newBalances["Liabilities"].append(accountBalanceLoop)


    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Historical Data")

    #Check to see if there is a file for historical data. If not, creates one.
    if 'Historical Data.csv' not in os.curdir:
        dataFile = open('Historical Data.csv', 'a', newline="")
        outputWriter = csv.writer(dataFile)
        outputWriter.writerow(['Date', 'Account Name', 'Account Balance'])
        dataFile.close()

    #Write the data to the csv before clearing it from Sqlite
    with open("Historical Data.csv", 'a', newline='') as csvfile:
        rowheaders = ['Date', 'Account Name', 'Account Balance']
        thewriter = csv.DictWriter(csvfile, fieldnames=rowheaders)
        today = datetime.date.today()
        for i in newBalances.values():
            print(i)
            for s in i:
                print(i)
                print(s)
                thewriter.writerow(
                {'Date': today, 'Account Name': newBalances[s], 'Account Balance': s})




    c.execute("UPDATE Assets SET \'Account Balance\'= ("+("?, "*(len(newBalances["Assets"])-1)+"?") +")", newBalances["Assets"])

    conn.commit()

    print("Balances Updated")
    mainDirectory()





def removeDatabaseColumn(accountType):
    import sqlite3, os
    #os.chdir("/home/doncapodilupo/.PyCharmCE2019.2/config/scratches/Personal Finance/Databases/")
    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Databases")
    conn = sqlite3.connect('Finances.db')
    c = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]

    print("What " + accountType + " would you like to remove from your Balance Sheet?")

    pluralDict = {"Asset": "Assets", "Liability": "Liabilities", "Income": "Incomes", "Expense": "Expenses"}
    accountTypePlural = pluralDict[accountType]  # Returns the plural version of "accountType" ex. Asset -> Assets

    #Converts the string so that it works with the SQL qwery.


    #Produces a numerical list based off of the desired sqlite column
    possibleChoices = [c.execute('SELECT * FROM '+accountTypePlural).fetchall()]
    acceptableChoices = []
    for i in possibleChoices:
        for s in i:
            acceptableChoices.append(s[2])
    acceptableChoices.append("Exit")        #Would like to shrink into one line. (you can't append a list to a list)

    #Prompts the user to select the item to remove from the database.
    userChoice = listDisplay(acceptableChoices)

    #remove data
    c.execute('DELETE FROM '+accountTypePlural+' WHERE Description = ?',(userChoice,)) #userChoice needs to be a tuple or it will throw a "no such column as userChoice"
    conn.commit()

    #Converts the string back so the confirmation sentences is grammatically correct.
    print("The " +accountTypePlural+" has been deleted")
    mainDirectory()

def addDatabaseColumn(accountType):
    import sqlite3, os, datetime
    # os.chdir("/home/doncapodilupo/.PyCharmCE2019.2/config/scratches/Personal Finance/Databases/") #Change directory so databases are localized
    os.chdir(
        "C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Databases")  # Change directory so databases are localized

    conn = sqlite3.connect('Finances.db')  # create a connection the database/create it if it doesn't exist.
    c = conn.cursor()  # no clue what this does specifically.

    #Ensure database name and proper grammar don't interrupt each other.
    pluralDict = {"Asset": "Assets", "Liability": "Liabilities", "Income": "Incomes", "Expense": "Expenses"}
    accountTypePlural = pluralDict[accountType]  # Returns the plural version of "accountType" ex. Asset -> Assets

    #Get user input and format it to be added to the SQLite database.
    newDBColumn = []  # This list will house all of my variables, lists work smoothly with SQLite
    today = str(datetime.date.today())#Each record will have the date recorded.

    print("Please give a description for the " + accountType + ".")
    assetDescription = input(">")
    print("What is the current value of the " + accountType + ".")
    assetaccountBalance = input(">")

    newDBColumn.append(today)
    newDBColumn.append(assetDescription)
    newDBColumn.append(assetaccountBalance)

    #Append the data to the proper table in the database. Confirm for the user. Return to main menu.
    c.execute("INSERT INTO " + accountTypePlural + " VALUES (NULL, ?, ?, ?)",
              newDBColumn)  # This line of code added a new row to the database.
    conn.commit()
    print(accountType + " has been added.")
    mainDirectory()

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

def decisionAccountType():
    acceptableChoices = ["Asset", "Liability","Income","Expense"]
    decision = listDisplay(acceptableChoices)
    return decision

def mainDirectory():
    print()

    acceptableChoices = ["Update Account Balances","Add a Record","Remove a Record","Manipulate Income/Expense",        #Need to add "See most upd to date financial data"
                         "Exit"]
    userChoice = listDisplay(acceptableChoices)

    if userChoice == acceptableChoices[0]:              #Update Account Balances
        print("Function is in \'intro.py\'")
    elif userChoice == acceptableChoices[1]:            #Add An Account
        addDatabaseColumn(decisionAccountType())  #Decide if the user is adding an asset or a liability Add the item to the appropriate database.
    elif userChoice == acceptableChoices[2]:            #Remove An Account
        removeDatabaseColumn(decisionAccountType())
    elif userChoice == acceptableChoices[3]:            #Manipulate Income/Expenses
        print("Function is in \'intro.py\'")                    #User decides bulk import or manual entry.
                                                        #Exit is handled in the listDisplay function.


print("Hell, Welcome to the Personal Finance Software V0.01")
print("At this time we assume you are Donald Capodilupo")
mainDirectory()

