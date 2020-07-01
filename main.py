from Classes.SetupPFinance import SetupTool
from Classes.ListDisplay import ListDisplay
from Classes.DatabaseRetrieval import *
from Dictionaries.PFinanceDicts import completeBalanceSheet
from Classes.CSVBackup import DatabaseBackup
import os
from os import path




#/home/user/Github_Files/Personal-Finance
ROOT = path.dirname(path.realpath(__file__))
print(ROOT)


if __name__ == "__main__":
    print("Hell, Welcome to the Personal Finance Software V1.00")
    accountSetup = SetupTool()

    mainMenuOptions = ["Update Account Balances","Add a Record","Remove a Record","View Current Balances"]
    dataBaseNames = ["Current_Assets.db", "NonCurrent_Assets.db", "Current_Liabilities.db", "NonCurrent_Liabilities.db"]


    while True:
        os.chdir(ROOT)
        mainMenuChoice = ListDisplay(mainMenuOptions)
        if mainMenuChoice == mainMenuOptions[0]:              #Update Account Balances
            backupDatabase = DatabaseBackup(ROOT)
            for dbName in dataBaseNames:
                dbToBeUpdated = DatabaseManipulation(dbName, ROOT)
                if "Assets" in dbName:
                    dbToBeUpdated.updateDatabaseColumns(completeBalanceSheet["Assets"][dbName][:-3])
                else:
                    dbToBeUpdated.updateDatabaseColumns(completeBalanceSheet["Liabilities"][dbName][:-3])

        elif mainMenuChoice == mainMenuOptions[1]:            #Add An Account
            print("What item would you like to add?\n")

            userChoiceGeneric = ListDisplay([*completeBalanceSheet], addExit=False)
            print("What is the term of the "+userChoiceGeneric+"?")

            accountTypeTerm = ListDisplay(completeBalanceSheet[userChoiceGeneric]).displayList(addExit=False)
            accountTypeFinal = ListDisplay(completeBalanceSheet[userChoiceGeneric][accountTypeTerm]).displayList(addExit=False)
            addRowObj = DatabaseManipulation((accountTypeTerm.replace(" ","_")+".db"),ROOT)
            addRowObj.addRow(accountTypeFinal)
        elif mainMenuChoice == mainMenuOptions[2]:
            print("What item would you like to remove?\n")

            accountTypeGeneric = ListDisplay([*completeBalanceSheet])
            userChoiceGeneric = accountTypeGeneric.displayList(addExit=False)
            print("What is the term of the " + userChoiceGeneric + "?")
            accountTypeTerm = ListDisplay(completeBalanceSheet[userChoiceGeneric]).displayList(addExit=False)
            accountTypeFinal = ListDisplay(completeBalanceSheet[userChoiceGeneric][accountTypeTerm]).displayList(
                addExit=False)
            addRowObj = DatabaseManipulation((accountTypeTerm.replace(" ", "_") + ".db"), ROOT)
            addRowObj.removeDatabaseRow(accountTypeFinal)
        #elif mainMenuChoice == mainMenuOptions[3]:
        #    import gspread
        #    from oauth2client.service_account import ServiceAccountCredentials
        #    from Classes.DatabaseRetrieval import DatabaseManipulation
        #    from Classes.ClassGoogleBalanceSheet import BalanceSheetUpdate
#
#
        #    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        #             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        #    import os
#
        #    obj = DatabaseManipulation("", ROOT)
        #    databaseDict = obj.getDatabaseInfoAsDict()
#
#
        #    creds = ServiceAccountCredentials.from_json_keyfile_name(
        #        "/home/doncapodilupo/Github_Files/Personal-Finance/Creds.json", scope)
        #    client = gspread.authorize(creds)
        #    sheet = client.open('Balance Sheet')
#
        #    balanceSheet = BalanceSheetUpdate(sheet,databaseDict)
        #    balanceSheet.addDatabaseToSpreadsheet()
        #    print("\nBalance sheet has been updated!\n")
        #    os.chdir(ROOT)




#TODO: Bug fix: user doesn't input a number, sql attacks ettc.
#TODO: Make the balance sheet look nicer, boarders, commas, dollar signs, percent change etc.
#TODO: Add try/excepts (or error handling) for when there is already a sheet with that name
