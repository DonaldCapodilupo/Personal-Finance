class DatabaseManipulation:
    def __init__(self, databaseName, mainDirectory):
        import os
        self.mainDirectory = mainDirectory
        self.databaseName = databaseName
        self.databaseDirectory = mainDirectory+"/Databases"



    def addRow(self, accountType):
        import sqlite3, datetime, os
        from Classes.AccountClasses import balance_Sheet_Item
        os.chdir(self.databaseDirectory)
        conn = sqlite3.connect(self.databaseName)  # create a connection the database/create it if it doesn't exist.
        c = conn.cursor()  # no clue what this does specifically.
        today = str(datetime.date.today())  # Each record will have the date recorded.
        print("Please give a description for the " + accountType + ".")
        assetDescription = str(input(">"))
        print("What is the current value of the " + accountType + ".")
        assetAccountBalance = str(input(">"))

        newRow = balance_Sheet_Item("No ID needed", assetDescription, assetAccountBalance)

        # Append the data to the proper table in the database. Confirm for the user. Return to main menu.
        c.execute("INSERT INTO " + accountType + " VALUES (NULL, ?, ?, ?)",
                  (today, newRow.accountNickName,
                   newRow.accountBalance))  # This line of code added a new row to the database.
        conn.commit()
        print(accountType + " has been added.\n")

    def removeDatabaseRow(self, accountType):
        import sqlite3, os
        os.chdir(self.databaseDirectory)
        conn = sqlite3.connect(self.databaseName)
        c = conn.cursor()
        conn.row_factory = lambda cursor, row: row[0]

        print("What " + accountType + " would you like to remove from your Balance Sheet?")

        # Produces a numerical list based off of the desired sqlite column
        possibleChoices = [c.execute('SELECT * FROM ' + accountType).fetchall()]
        acceptableChoices = []
        for i in possibleChoices:
            for s in i:
                acceptableChoices.append(s[2])


        # Prompts the user to select the item to remove from the database.
        from Classes.ListDisplay import ListDisplay
        userChoice = ListDisplay(acceptableChoices).displayList(addExit=False)

        # remove data
        c.execute('DELETE FROM ' + accountType + ' WHERE Description = ?',
                  (userChoice,))  # userChoice needs to be a tuple or it will throw a "no such column as userChoice"
        conn.commit()

        # Converts the string back so the confirmation sentences is grammatically correct.
        print(userChoice + " has been deleted from " + accountType)

    def updateDatabaseColumns(self, tableList):
        import os, sqlite3
        os.chdir(self.databaseDirectory)
        conn = sqlite3.connect(self.databaseName)  # create a connection the database/create it if it doesn't exist.
        c = conn.cursor()  # no clue what this does specifically.
        for table in tableList:
            for row in c.execute('SELECT * FROM ' + table + ' ORDER BY ID').fetchall():
                from Classes.AccountClasses import balance_Sheet_Item
                print("What is the current balance of " + str(row[2]) + "?")
                accountBalanceLoop = input(">")
                account = balance_Sheet_Item((str(row[0])), (str(row[2])), accountBalanceLoop)
                c.execute("UPDATE " + table + " SET Value =" + account.accountBalance + " WHERE ID = " + account.accountID)
                conn.commit()
        print("\n"+self.databaseName+" Updated")



    def getDatabaseInfoAsDict(self):
        import sqlite3, os
        os.chdir(self.databaseDirectory)
        from Dictionaries.PFinanceDicts import completeBalanceSheet, balanceSheetSpecificToGeneral
        dataBaseNames = ["Current_Assets.db", "NonCurrent_Assets.db", "Current_Liabilities.db",
                         "NonCurrent_Liabilities.db"]
        rowObjDict = {}


        for db in dataBaseNames:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            conn.row_factory = lambda cursor, row: row[0]
            if db == "Current_Assets.db":
                for table in completeBalanceSheet["Assets"]["Current Assets"]:
                    for row in c.execute('SELECT * FROM ' + table + ' ORDER BY ID').fetchall():
                        from Classes.AccountClasses import balance_Sheet_Item
                        dictObj = balance_Sheet_Item(row[0],row[1],row[2])
                        try:
                            rowObjDict[db].append(
                                [dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID])
                        except KeyError:
                            rowObjDict.update({db:[dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID]})

            elif db == "NonCurrent_Assets.db":
                for table in completeBalanceSheet["Assets"]["NonCurrent Assets"]:
                    for row in c.execute('SELECT * FROM ' + table + ' ORDER BY ID').fetchall():
                        from Classes.AccountClasses import balance_Sheet_Item
                        dictObj = balance_Sheet_Item(row[0],row[1],row[2])
                        try:
                            rowObjDict[db].append(
                                [dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID])
                        except KeyError:
                            rowObjDict.update({db: [dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID]})
            elif db == "Current_Liabilities.db":
                for table in completeBalanceSheet["Liabilities"]["Current Liabilities"]:
                    for row in c.execute('SELECT * FROM ' + table + ' ORDER BY ID').fetchall():
                        from Classes.AccountClasses import balance_Sheet_Item
                        dictObj = balance_Sheet_Item(row[0],row[1],row[2])
                        try:
                            rowObjDict[db].append(
                                [dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID])
                        except KeyError:
                            rowObjDict.update({db: [dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID]})
            elif db == "NonCurrent_Liabilities.db":
                for table in completeBalanceSheet["Liabilities"]["NonCurrent Liabilities"]:
                    for row in c.execute('SELECT * FROM ' + table + ' ORDER BY ID').fetchall():
                        from Classes.AccountClasses import balance_Sheet_Item
                        dictObj = balance_Sheet_Item(row[0],row[1],row[2])
                        try:
                            rowObjDict[db].append(
                                [dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID])
                        except KeyError:
                            rowObjDict.update({db: [dictObj.accountBalance, dictObj.accountNickName, dictObj.accountID]})
        return rowObjDict




           # acceptableChoices = []
           # for i in possibleChoices:
           #     for s in i:
           #         acceptableChoices.append(s[2])





