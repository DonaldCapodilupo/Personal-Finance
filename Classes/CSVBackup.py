class DatabaseBackup:
    def __init__(self, mainDirectory):
        self.mainDirectory = mainDirectory
        self.directory = mainDirectory +"/Historical Data"
        self.databaseDirectory = mainDirectory+"/Databases"

    def updateCSV(self, lineItem):
        import os
        import csv, datetime
        today = datetime.date.today()  # Records the date that the account balances were updated.
        os.chdir(self.directory)
        with open('Historical Data.csv', 'a', newline='') as csvFile:
            outputWriter = csv.writer(csvFile)
            row = [today, lineItem.accountNickName, lineItem.accountBalance]
            outputWriter.writerow(row)

    def createCSVObject(self, row):
        from Classes.AccountClasses import balance_Sheet_Item
        lineItem = balance_Sheet_Item("Null", row[2], row[3])
        DatabaseBackup.updateCSV(self, lineItem)

    def getCSVData(self, db, appropriateTableList):
        import sqlite3
        conn = sqlite3.connect(db)  # create a connection the database/create it if it doesn't exist.
        c = conn.cursor()  # no clue what this does specifically.
        for table in appropriateTableList:
            # Append both the "Account Name" and  "'Current' Account Balance" to separate lists.
            for row in c.execute('SELECT * FROM ' + table + ' ORDER BY Description'):
                DatabaseBackup.createCSVObject(self, row)

    def updateHistoricalCSV(self):
        from os import path
        print("Backing up current account balances to " + self.directory)
        # Connect to the database to get asset/liability names.
        dataBaseNames = ["Current_Assets.db", "NonCurrent_Assets.db", "Current_Liabilities.db",
                         "NonCurrent_Liabilities.db"]
        from Dictionaries.PFinanceDicts import completeBalanceSheet
        for db in dataBaseNames:
            if db == 'Current_Assets.db':
                self.getCSVData(path.join(self.databaseDirectory,db), completeBalanceSheet["Assets"]["Current Assets"])
                print("Current Assets have been backed up.")
            elif db == 'NonCurrent_Assets.db':
                self.getCSVData(path.join(self.databaseDirectory, db), completeBalanceSheet["Assets"]["NonCurrent Assets"])
                print("NonCurrent Assets have been backed up.")
            elif db == 'Current_Liabilities.db':
                self.getCSVData(path.join(self.databaseDirectory, db), completeBalanceSheet["Liabilities"]["Current Liabilities"])
                print("Current Liabilities have been backed up.")
            elif db == 'NonCurrent_Liabilities.db':
                self.getCSVData(path.join(self.databaseDirectory, db), completeBalanceSheet["Liabilities"]["NonCurrent Liabilities"])
                print("NonCurrent Liabilities have been backed up.")