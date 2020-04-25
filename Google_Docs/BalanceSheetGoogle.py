class BalanceSheetItem:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


def getWorksheetTitle():
    import datetime
    current_time = datetime.datetime.now()
    worksheetTitle = current_time.strftime('%m%d%y')
    return worksheetTitle


def setupGoogleSpreadsheet(dictOfDBRowObjects):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    import os
    os.chdir("/home/doncapodilupo/Github_Files/Personal-Finance/Google_Docs")

    creds = ServiceAccountCredentials.from_json_keyfile_name("", scope)

    client = gspread.authorize(creds)

    sh = client.open('Balance Sheet')

    worksheet = sh.add_worksheet(title=getWorksheetTitle(),rows="100", cols="7")

    worksheet.merge_cells("A1:E1")
    worksheet.update_cell(1, 1, getWorksheetTitle())
    worksheet.format("A1:E2", {"horizontalAlignment":"CENTER"})

    worksheet.update_cell(2, 1, "Current Assets:")
    worksheet.update_cell(2, 5, "Change %")


    s = 3
    for i in dictOfDBRowObjects["Current_Assets.db"]:
        worksheet.update_cell(s, 3, i[1])
        worksheet.update_cell(s, 4, i[0])
        s+=1

    s +=3

    worksheet.update_cell(s-1, 1, "Non Current Assets:")
    for i in dictOfDBRowObjects["NonCurrent_Assets.db"]:
        worksheet.update_cell(s, 3, i[1])
        worksheet.update_cell(s, 4, i[0])
        s += 1




    s += 1
    worksheet.format("A1:E" + str(s) + "", {"backgroundColor": {"red": 0.0,
                                                                                 "green": 1.0, "blue": 5.0}})
    firstLiabilityRow = (str(s+1))
    s+=2

    worksheet.update_cell(s - 1, 1, "Current Liabilities:")
    for i in dictOfDBRowObjects["Current_Liabilities.db"]:
        worksheet.update_cell(s, 3, i[1])
        worksheet.update_cell(s, 4, i[0])
        s += 1



    s += 3

    worksheet.update_cell(s - 1, 1, "Non Current Liabilities:")
    for i in dictOfDBRowObjects["NonCurrent_Liabilities.db"]:
        worksheet.update_cell(s, 3, i[1])
        worksheet.update_cell(s, 4, i[0])
        s += 1

    worksheet.format("A"+firstLiabilityRow+":E" + str(s) + "", {"backgroundColor": {"red": 5.0,
                                                                    "green": 0.1, "blue": 0.0}})
    s += 1

    worksheet.update_cell(s, 1, "Equity:")
    worksheet.update_cell(s, 4,"Equity Amount")


    lastLiabilityRow = (str(s))
    worksheet.format("A" + lastLiabilityRow + ":E" + str(s) + "", {"backgroundColor": {"red": 0.0,
                                                                                        "green": 1.0, "blue": 0.1}})

    s += 1

    worksheet.merge_cells("A"+str(s)+":E"+str(s))
    worksheet.update_cell(s, 1, "Notable Events")
    worksheet.format("A"+str(s)+":E"+str(s), {"horizontalAlignment":"CENTER"})

    s += 1

    worksheet.merge_cells("A" + str(s) + ":E" + str(s+5))

    print("Where there any notable events?")
    worksheet.update_cell(s, 1, input(">"))