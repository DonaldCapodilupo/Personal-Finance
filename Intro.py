

def addRecord(decision):
    import sqlite3, os

    #os.chdir("/home/doncapodilupo/.PyCharmCE2019.2/config/scratches/Personal Finance/Databases/") #Change directory so databases are localized
    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Databases")  # Change directory so databases are localized

    conn = sqlite3.connect('Finances.db')  # create a connection the database/create it if it doesn't exist.
    c = conn.cursor()  # no clue what this does specifically.

    #Get
    acceptableChoices = [c.execute('SELECT id FROM users').fetchall()]
    for i in acceptableChoices:
        print(i)

def decideIncomeExpense():
    acceptableChoices = ["Income","Expense"]
    userChoice = listDisplay(acceptableChoices)

    if userChoice == acceptableChoices[0]:
        return acceptableChoices[0]
    elif userChoice == acceptableChoices[1]:
        return acceptableChoices[1]

#This function takes a list of strings and displays them in a numerical list. If the user enters an invalid number,
#the function loops. It returns the users choice is a string (Helpful for debugging) or exit the program of that is an option
#the list
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

def decisionManualorAutomatic():
    acceptableChoices = ["Bulk Import from a Bank Statement","Manually Add/Remove an Income/Expense","Exit"]
    userChoice =  listDisplay(acceptableChoices)


    if userChoice == acceptableChoices[0]:
        print("This option will take you to an \"everything is downloaded, right?\" function. ")
    elif userChoice == acceptableChoices[1]:
        addRecord(decideIncomeExpense())


###########This is some sample data. I might need to have a dict parameter to the function?#############################
def visualizeData():
    #import plotly.express as px
    #import pandas as pd

    #wide_df = pd.DataFrame(
    #    dict(Month=["Last months Assets, Liabilities and Equity.", "Current months Assets, Liabilites and Equity", ],
    #         Assets=[100, 75],
    #         Liabilities=[80, 120],
    #         Equity=[50, 75]))
    #tidy_df = wide_df.melt(id_vars="Month")

    #fig = px.bar(tidy_df, x="Month", y="Monetary Value", color="variable", barmode="group")
    #fig.show()
    quit()
########################################################################################################################


######THIS NEEDS TO BE COMPLETED. CURRENTLY STUCK AT UPDATING ACCOUNT BALANCE FIGURES IN DATABASE######################
def updateAccounts():
    import sqlite3, os, csv, datetime
    #os.chdir("/home/doncapodilupo/.PyCharmCE2019.2/config/scratches/Personal Finance/Databases/")  # Change directory so databases are localized
    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Databases")

    conn = sqlite3.connect('Finances.db')  # create a connection the database/create it if it doesn't exist.
    c = conn.cursor()  # no clue what this does specifically.

    newBalances = {"Assets":[],"Liabilities":[]}


    for row in c.execute('SELECT * FROM Assets ORDER BY id'):
        print("What is the current balance of "+ str(row[2]+"?"))
        accountBalanceLoop = input(">")
        newBalances["Assets"].append(accountBalanceLoop)
    for row in c.execute('SELECT * FROM Liabilities ORDER BY id'):
        print("What is the current balance of "+ str(row[2]+"?"))
        accountBalanceLoop = input(">")
        newBalances["Liabilities"].append(accountBalanceLoop)


    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Historical Data")

    if 'Historical Data.csv' not in os.curdir:
        dataFile = open('Historical Data.csv', 'a', newline="")
        outputWriter = csv.writer(dataFile)
        outputWriter.writerow(['Date', 'Account Name', 'Account Balance'])
        dataFile.close()


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
######################################################################################################################

def decisionRemoveAssetLiability():
    print("Are you working with an Asset or a Liability?")
    apropriateChoices = ["Asset", "Liability"]
    decision = listDisplay(apropriateChoices)
    return decision

def decisionAddAssetLiability():
    acceptableChoices = ["Asset", "Liability"]
    decision = listDisplay(acceptableChoices)
    return decision

def addAccount(decision):
    import sqlite3, os, datetime

    #os.chdir("/home/doncapodilupo/.PyCharmCE2019.2/config/scratches/Personal Finance/Databases/") #Change directory so databases are localized
    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Databases")  # Change directory so databases are localized

    conn = sqlite3.connect('Finances.db')  # create a connection the database/create it if it doesn't exist.
    c = conn.cursor() #no clue what this does specifically.

    today = datetime.date.today()

    newAsset = [] #This list will house all of my variables, lists work smoothly with SQLite

    print("Please give a description for the "+decision+".")
    assetDescription = input(">")
    print("What is the current value of the "+decision+".")
    assetaccountBalance = input(">")


    newAsset.append(str(today))
    newAsset.append(assetDescription)
    newAsset.append(assetaccountBalance)

    if decision == "Asset":
        decision = "Assets"
    if decision == "Liability":
        decision = "Liabilities"
    c.execute("INSERT INTO "+decision+" VALUES (NULL, ?, ?, ?)", newAsset) #This line of code added a new row to the database.
    conn.commit()
    if decision == "Assets":
        decision = "Asset"
    if decision == "Liabilities":
        decision = "Liability"
    print(decision +" has been added.")
    mainDirectory()

def removeAccount(decision):
    import sqlite3, os
    #os.chdir("/home/doncapodilupo/.PyCharmCE2019.2/config/scratches/Personal Finance/Databases/")
    os.chdir("C:\\Users\Snaps\.PyCharmCE2018.3\config\scratches\Personal Finance\Databases")
    conn = sqlite3.connect('Finances.db')
    c = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]

    print("What " + decision + " would you like to remove from your Balance Sheet?")

    #Converts the string so that it works with the SQL qwery.
    if decision == "Asset":
        decision = "Assets"
    if decision == "Liability":
        decision = "Liabilities"

    #Produces a numerical list based off of the desired sqlite column
    possibleChoices = [c.execute('SELECT * FROM '+decision).fetchall()]
    acceptableChoices = []
    for i in possibleChoices:
        for s in i:
            acceptableChoices.append(s[2])
    acceptableChoices.append("Exit")        #Would like to shrink into one line. (you can't append a list to a list)

    #Prompts the user to select the item to remove from the database.
    userChoice = listDisplay(acceptableChoices)

    #remove data
    c.execute('DELETE FROM '+decision+' WHERE Description = ?',(userChoice,)) #userChoice needs to be a tuple or it will throw a "no such column as userChoice"
    conn.commit()

    #Converts the string back so the confirmation sentences is grammatically correct.
    if decision == "Assets":
        decision = "Asset"
    if decision == "Liabilities":
        decision = "Liability"
    print("The " +decision+" has been deleted")
    mainDirectory()

def mainDirectory():
    print()

    acceptableChoices = ["Update Account Balances","Add an Account","Remove an Account","Manipulate Income/Expense",
                         "Exit"]
    userChoice = listDisplay(acceptableChoices)

    if userChoice == acceptableChoices[0]:              #Update Account Balances
        updateAccounts() #Not yet complete
    elif userChoice == acceptableChoices[1]:            #Add An Account
        addAccount(decisionAddAssetLiability())           #Decide if the user is adding an asset or a liability Add the item to the appropriate database.
    elif userChoice == acceptableChoices[2]:            #Remove An Account
        removeAccount(decisionRemoveAssetLiability())
    elif userChoice == acceptableChoices[3]:            #Manipulate Income/Expenses
        decisionManualorAutomatic()                     #User decides bulk import or manual entry.
                                                        #Exit is handled in the listDisplay function.


print("Hell, Welcome to the Personal Finance Software V0.01")
print("At this time we assume you are Donald Capodilupo")
mainDirectory()