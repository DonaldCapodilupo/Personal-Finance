from Classes.SetupPFinance import SetupTool
from Classes.ListDisplay import ListDisplay
from Classes.DatabaseRetrieval import *
from Dictionaries.PFinanceDicts import completeBalanceSheet



if __name__ == "__main__":
    print("Hell, Welcome to the Personal Finance Software V1.10")
    accountSetup = SetupTool
    accountSetup.directorySetup()
    accountSetup.databaseSetup()


    mainMenuOptions = ["Update Account Balances","Add a Record","Remove a Record","View Current Balances"]
    mainMenu = ListDisplay(mainMenuOptions)
    while True:
        userChoice = mainMenu.displayList(addExit=True)
        if userChoice == mainMenuOptions[0]:              #Update Account Balances
            #Need to add a function to back up to "Historical CSV" directory
            dataBaseNames = ["Current_Assets.db", "NonCurrent_Assets.db", "Current_Liabilities.db", "NonCurrent_Liabilities.db"]
            for dbName in dataBaseNames:
                dbToBeUpdated = DatabaseManipulation(dbName)
                if "Assets" in dbName:
                    dbToBeUpdated.updateDatabaseColumns(completeBalanceSheet["Assets"][(dbName.replace("_"," ")[:-3])])
                else:
                    dbToBeUpdated.updateDatabaseColumns(completeBalanceSheet["Liabilities"][(dbName.replace("_"," ")[:-3])])

        elif userChoice == mainMenuOptions[1]:            #Add An Account
            print("What item would you like to add?\n")
            accountTypeGeneric = ListDisplay([*completeBalanceSheet])
            userChoiceGeneric = accountTypeGeneric.displayList(addExit=False)
            print("What is the term of the "+userChoiceGeneric+"?")
            accountTypeTerm = ListDisplay(completeBalanceSheet[userChoiceGeneric]).displayList(addExit=False)
            accountTypeFinal = ListDisplay(completeBalanceSheet[userChoiceGeneric][accountTypeTerm]).displayList(addExit=False)
            addRowObj = DatabaseManipulation((accountTypeTerm.replace(" ","_")+".db"))
            addRowObj.addRow(accountTypeFinal)
        elif userChoice == mainMenuOptions[2]:
            print("What item would you like to remove?\n")
            accountTypeGeneric = ListDisplay([*completeBalanceSheet])
            userChoiceGeneric = accountTypeGeneric.displayList(addExit=False)
            print("What is the term of the " + userChoiceGeneric + "?")
            accountTypeTerm = ListDisplay(completeBalanceSheet[userChoiceGeneric]).displayList(addExit=False)
            accountTypeFinal = ListDisplay(completeBalanceSheet[userChoiceGeneric][accountTypeTerm]).displayList(
                addExit=False)
            addRowObj = DatabaseManipulation((accountTypeTerm.replace(" ", "_") + ".db"))
            addRowObj.removeDatabaseRow(accountTypeFinal)
        elif userChoice == mainMenuOptions[3]:
            pass


        #elif userChoice == mainMenuOptions[2]:            #Remove An Account
        #    removeDatabaseRow(decisionAccountType())
        #elif userChoice == mainMenuOptions[3]:  # Remove An Account
        #    displayTotals()