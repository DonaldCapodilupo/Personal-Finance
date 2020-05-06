

def getWorksheetTitle():
    import datetime
    current_time = datetime.datetime.now()
    worksheetTitle = current_time.strftime('%m%d%y')
    return worksheetTitle


def getDictTotals(dictKeyDatabase):
    s = 0
    try:
        for i in dictKeyDatabase:
            s += float(i[0])
    except KeyError:
        pass
    return s


class BalanceSheetUpdate:
    def __init__(self, worksheet, dbDict):
        self.worksheet = worksheet
        self.itr = 3
        self.databases = ["Current_Assets.db","NonCurrentAssets.db",
                          "Current_Liabilities.db","NonCurrent_Liabilities.db"]
        self.dbDict = dbDict

    def addDatabaseToSpreadsheet(self):

        self.worksheet = self.worksheet.add_worksheet(title=getWorksheetTitle(), rows="100", cols="7")

        self.worksheet.merge_cells("A1:E1")
        self.worksheet.update_cell(1, 1, getWorksheetTitle())
        self.worksheet.format("A1:E2", {"horizontalAlignment": "CENTER"})

        for db in self.databases:
            self.worksheet.update_cell(self.itr, 1,str(db[:-3])) # Current_Assets
            self.itr += 1
            try:
                for lineItem in self.dbDict[db]:
                    self.worksheet.update_cell(self.itr, 3, lineItem[1]) #Wallet Cash
                    self.worksheet.update_cell(self.itr, 4, lineItem[0]) #25.25
                    self.itr += 1
            except KeyError:
                pass
            self.itr += 1
            self.worksheet.update_cell(self.itr, 1, "Total "+str(db[:-3])) #Total for Current_Assets
            try:
                self.worksheet.update_cell(self.itr, 4, (getDictTotals(self.dbDict[db]))) #=25.25+1+1...etc
            except KeyError:
                self.worksheet.update_cell(self.itr, 4, "0.00")
            self.itr += 2

        self.worksheet.merge_cells("A" + str(self.itr) + ":E" + str(self.itr))
        self.worksheet.update_cell(self.itr, 1, "Notable Events")
        self.worksheet.format("A" + str(self.itr) + ":E" + str(self.itr), {"horizontalAlignment": "CENTER"})

        self.itr += 1


        self.worksheet.merge_cells("A" + str(self.itr) + ":E" + str(self.itr + 5))

        print("Where there any notable events?")
        self.worksheet.update_cell(self.itr, 1, input(">"))
