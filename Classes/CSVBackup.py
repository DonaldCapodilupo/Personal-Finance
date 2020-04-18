
class DatabaseBackup:
    def __init__(self):
        import os
        self.directory = os.getcwd()+"/Historical Data"

    def updateCSV(self, lineItem):
        import csv, datetime
        today = datetime.date.today()  # Records the date that the account balances were updated.
        os.chdir(csvHistoryDirectory)
        with open('Historical Data.csv', 'a', newline='') as csvfile:
            outputWriter = csv.writer(csvfile)
            row = [today, lineItem.accountNickName, lineItem.accountBalance]
            outputWriter.writerow(row)
    def createCSVObject(self, row):
        from Classes.AccountClasses import balance_Sheet_Item
        lineItem = balance_Sheet_Item("Null", row[2], row[3])
        updateCSV(lineItem)
    def getCSVData(self, db, appropriateTableList):
        os.chdir(databaseDirectory)
        conn = sqlite3.connect(db)  # create a connection the database/create it if it doesn't exist.
        c = conn.cursor()  # no clue what this does specifically.
        for table in appropriateTableList:
            # Append both the "Account Name" and  "'Current' Account Balance" to separate lists.
            for row in c.execute('SELECT * FROM ' + table + ' ORDER BY Description'):
                createCSVObject(row)