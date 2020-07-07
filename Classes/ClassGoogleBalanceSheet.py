def getWorksheetTitle():
    import datetime
    current_time = datetime.datetime.now()
    worksheetTitle = current_time.strftime('%m%d%y')
    return worksheetTitle

def sumAccounts(accountDicts):
    try:
        accountTotal = [sum(int(row[0]) for row in accountDicts["Current_Assets.db"]) for i in range(len(accountDicts["Current_Assets.db"]))]
        return accountTotal
    except KeyError:
        return 0.00


class BalanceSheetUpdate:
    def __init__(self, worksheet, dbDict):
        self.worksheet = worksheet
        self.lastAssetRow = 1
        self.databases = ["Current_Assets.db","NonCurrent_Assets.db",
                          "Current_Liabilities.db","NonCurrent_Liabilities.db"]
        self.dbDict = dbDict
        self.totalsDict = {"Current_Assets.db": [sum(int(row[0]) for row in dbDict["Current_Assets.db"]) for i in range(len(dbDict["Current_Assets.db"]))],
                           "NonCurrent_Assets.db":[sum(int(row[0]) for row in dbDict["NonCurrent_Assets.db"]) for i in range(len(dbDict["NonCurrent_Assets.db"]))],
                           "Current_Liabilities.db":[sum(int(row[0]) for row in dbDict["Current_Liabilities.db"]) for i in range(len(dbDict["Current_Liabilities.db"]))],
                           "NonCurrent_Liabilities.db":[sum(int(row[0]) for row in dbDict["NonCurrent_Liabilities.db"]) for i in range(len(dbDict["NonCurrent_Liabilities.db"]))],
                           }
        self.equity = "Equity"


    def addDatabaseToSpreadsheet(self):

        self.worksheet = self.worksheet.add_worksheet(title=getWorksheetTitle(), rows="100", cols="7")
        self.worksheet.merge_cells("A1:E1")
        self.worksheet.update_cell(1, 1, getWorksheetTitle())
        self.worksheet.format("A1:E2", {"horizontalAlignment": "CENTER"})
        self.worksheet.update_cell(3, 5, "Change from previous Balance Sheet")

        cellRow = 4

        for db in self.databases:
            self.worksheet.update_cell(cellRow, 1,str(db[:-3])) # Current_Assets
            cellRow += 1
            try:
                for lineItem in self.dbDict[db]:
                    self.worksheet.update_cell(cellRow, 3, lineItem[1]) #Wallet Cash
                    self.worksheet.update_cell(cellRow, 4, lineItem[0]) #25.25
                    cellRow += 1
            except KeyError:
                pass
            cellRow += 1
            self.worksheet.update_cell(cellRow, 1, "Total for "+str(db[:-3])) #Total for Current_Assets
            #Totals amount. If no accounts, then the balance is zero
            try:
                self.worksheet.update_cell(cellRow, 4, self.totalsDict[db][0]) #=25.25+1+1...etc
            except KeyError:
                self.worksheet.update_cell(cellRow, 4, "0.00")
            cellRow +=1
            if db == "NonCurrent_Assets.db" or db == "NonCurrent_Liabilities.db":
                cellRow += 1
                self.worksheet.update_cell(cellRow, 1, "Total")
                try:
                    self.worksheet.update_cell(cellRow, 4, ((self.totalsDict[db][0]) + (self.totalsDict[db[3:]][0])))
                except KeyError:
                    self.worksheet.update_cell(cellRow, 4, "0.00")
                if self.lastAssetRow == 1:
                    self.worksheet.format("A"+str(self.lastAssetRow)+":E" + str(cellRow), {"backgroundColor": {"red": 0.0,
                                                                                   "green": 0.1,
                                                                                   "blue": 5.0}})
                else:
                    self.worksheet.format("A" + str(self.lastAssetRow) + ":E" + str(cellRow),
                                          {"backgroundColor": {"red": 5.0,
                                                               "green": 0.1,
                                                               "blue": 0.0}})
                self.lastAssetRow = cellRow + 1
            cellRow += 1


        self.worksheet.update_cell(cellRow, 1, "Equity")
        self.worksheet.update_cell(cellRow, 4, (sum(self.totalsDict["Current_Assets.db"]+self.totalsDict["NonCurrent_Assets.db"])
                                                    - sum(self.totalsDict["Current_Liabilities.db"]+self.totalsDict["NonCurrent_Liabilities.db"])))
        self.worksheet.format("A" + str(cellRow) + ":E" + str(cellRow) + "",
                              {"backgroundColor": {"red": 0.0,"green": 5.0,"blue": 0.0}})
        cellRow += 1

        self.worksheet.merge_cells("A" + str(cellRow) + ":E" + str(cellRow))
        self.worksheet.update_cell(cellRow, 1, "Notable Events")
        self.worksheet.format("A" + str(cellRow) + ":E" + str(cellRow), {"horizontalAlignment": "CENTER"})
        cellRow += 1
        self.worksheet.merge_cells("A" + str(cellRow) + ":E" + str(cellRow + 5))
        print("Where there any notable events?")
        self.worksheet.update_cell(cellRow, 1, input(">"))