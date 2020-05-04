class BalanceSheetItem:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


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



def setupGoogleSpreadsheet(dictOfDBRowObjects):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    import os
    os.chdir("/home/doncapodilupo/Github_Files/Personal-Finance/Google_Docs")

    creds = ServiceAccountCredentials.from_json_keyfile_name("../../../.PyCharmCE2019.3/config/scratches/Creds.json", scope)

    client = gspread.authorize(creds)

    sh = client.open('Balance Sheet')

    worksheet = sh.add_worksheet(title=getWorksheetTitle(),rows="100", cols="7")

    worksheet.merge_cells("A1:E1")
    worksheet.update_cell(1, 1, getWorksheetTitle())
    worksheet.format("A1:E2", {"horizontalAlignment":"CENTER"})

    worksheet.update_cell(2, 1, "Current Assets:")
    worksheet.update_cell(2, 5, "Change %")


    s = 3
    try:
        for i in dictOfDBRowObjects["Current_Assets.db"]:
            worksheet.update_cell(s, 3, i[1])
            worksheet.update_cell(s, 4, i[0])
            s+=1

        s += 1
    except KeyError:
        pass
    worksheet.update_cell(s, 1, "Total Current Assets: ")
    try:
        worksheet.update_cell(s, 4, getDictTotals(dictOfDBRowObjects["Current_Assets.db"]))
    except KeyError:
        worksheet.update_cell(s, 4, 0.00)

    s +=3

    worksheet.update_cell(s-1, 1, "Non Current Assets:")
    try:
        for i in dictOfDBRowObjects["NonCurrent_Assets.db"]:
            worksheet.update_cell(s, 3, i[1])
            worksheet.update_cell(s, 4, i[0])
            s += 1
    except KeyError:
        pass

    s +=1
    worksheet.update_cell(s, 1, "Total NonCurrent Assets: ")

    try:
        worksheet.update_cell(s, 4, getDictTotals(dictOfDBRowObjects["NonCurrent_Assets.db"]))
    except KeyError:
        worksheet.update_cell(s, 4, 0.00)

    s += 2

    worksheet.update_cell(s, 1, "Total Assets: ")
    worksheet.update_cell(s, 4, (getDictTotals(dictOfDBRowObjects["Current_Assets.db"]))+
                                 getDictTotals(dictOfDBRowObjects["NonCurrent_Assets.db"]))



    s += 1
    worksheet.format("A1:E" + str(s) + "", {"backgroundColor": {"red": 0.0,
                                                                                 "green": 1.0, "blue": 5.0}})
    firstLiabilityRow = (str(s+1))
    s+=2

    try:
        worksheet.update_cell(s - 1, 1, "Current Liabilities:")
        for i in dictOfDBRowObjects["Current_Liabilities.db"]:
            worksheet.update_cell(s, 3, i[1])
            worksheet.update_cell(s, 4, i[0])
            s += 1
    except KeyError:
        pass

    s += 1

    worksheet.update_cell(s, 1, "Total Current Liabilities: ")
    worksheet.update_cell(s, 4, getDictTotals(dictOfDBRowObjects["Current_Liabilities.db"]))


    s += 3

    try:
        worksheet.update_cell(s - 1, 1, "Non Current Liabilities:")
        for i in dictOfDBRowObjects["NonCurrent_Liabilities.db"]:
            worksheet.update_cell(s, 3, i[1])
            worksheet.update_cell(s, 4, i[0])
            s += 1
    except KeyError:
        pass

    s += 1
    worksheet.update_cell(s, 1, "Total NonCurrent Liabilities: ")
    worksheet.update_cell(s, 4, getDictTotals(dictOfDBRowObjects["NonCurrent_Liabilities.db"]))


    s += 2

    worksheet.update_cell(s, 1, "Total Liabilities: ")
    worksheet.update_cell(s, 4, (getDictTotals(dictOfDBRowObjects["Current_Liabilities.db"])+
                                 getDictTotals(dictOfDBRowObjects["NonCurrent_Liabilities.db"])))



    worksheet.format("A"+firstLiabilityRow+":E" + str(s) + "", {"backgroundColor": {"red": 5.0,
                                                                    "green": 0.1, "blue": 0.0}})
    s += 1

    worksheet.update_cell(s, 1, "Equity:")
    worksheet.update_cell(s, 4,(
            (getDictTotals(dictOfDBRowObjects["Current_Assets.db"])+getDictTotals(dictOfDBRowObjects["NonCurrent_Assets.db"]))-
            (
            (getDictTotals(dictOfDBRowObjects["Current_Liabilities.db"])+getDictTotals(dictOfDBRowObjects["NonCurrent_Liabilities.db"]))
            )
    )
)



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