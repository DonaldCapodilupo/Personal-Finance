class BalanceSheetItem:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


def getWorksheetTitle():
    import datetime
    current_time = datetime.datetime.now()
    worksheetTitle = current_time.strftime('%m%d%y')
    return worksheetTitle


rowObjDict = {"Current Assets": [ ],
              "NonCurrent Assets": [],
              "Current Liabilities": [],
              "NonCurrent Liabilities": []}


def setupGoogleSpreadsheet(dictOfDBRowObjects):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("Creds.json", scope)

    client = gspread.authorize(creds)

    sh = client.open('Balance Sheet')

    worksheet = sh.add_worksheet(title=getWorksheetTitle(),rows="100", cols="7")


    worksheet.update_cell(1, 3, getWorksheetTitle())
    worksheet.update_cell(2, 1, "Current Assets:")

    s = 3
    for i in dictOfDBRowObjects:
        worksheet.update_cell(s, 3, i.name)
        worksheet.update_cell(s, 4, i.balance)
        s+=1

    s +=4
    worksheet.update_cell(s-1, 1, "Current Liabilities:")
    for i in objDict["Current Liabilities"]:
        worksheet.update_cell(s, 3, i.name)
        worksheet.update_cell(s, 4, i.balance)
        s += 1




