
class GoogleBalanceSheet:



    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import datetime
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("Creds.json", scope)

    client = gspread.authorize(creds)

    sh = client.open('Balance Sheet')

    worksheettitle = input("Sheet Title:  ")
    worksheet = sh.add_worksheet(title=worksheettitle, rows="100", cols="7")

    today = datetime.date.today()

    #Using the sheetname as a "date" for the time being.
    worksheet.update_cell(1,3, worksheettitle)


    #Asset Calculations
    worksheet.update_cell(4,4, input('How much Cash do you have on hand:'))
    worksheet.update_cell(5,4, input('How much is in ACU Account 2188: '))
    worksheet.update_cell(6,4, input('How much is in ACU Account 3393: '))
    worksheet.update_cell(7,4, input('How much is in ACU Account 1005: '))
    worksheet.update_cell(8,4, input('How much is in DCU Account 7295: '))
    worksheet.update_cell(9,4, input('How much is in Ally Account 7713: '))
    worksheet.update_cell(10,4, input('How much is in DCU Account 7105: '))
    worksheet.update_cell(13,4, "=sum(D4:D10)") # Total Cash Assets
    worksheet.update_cell(21,4, "=sum(D16:D19)") #Total Accounts Recievable
    worksheet.update_cell(32,4, "=sum(D24:D30)") #Total Physical Assets
    worksheet.update_cell(37,4, "=D35") #Total Business Assets
    worksheet.update_cell(39,4, '=D13+D21+D32+D37')  #Total Current Assets
    worksheet.update_cell(49,4, '=sum(D44:D47)') #Total Investments
    worksheet.update_cell(56,4, '=sum(D52:D54)') #Total Collections
    worksheet.update_cell(58,4, '=D49+D56') #Total Long Term Assets
    worksheet.update_cell(60,4, '=D39+D58') #Total Assets


    #Liability Calculations
    worksheet.update_cell(65,4, input('Ally Credit Card:'))
    worksheet.update_cell(66,4, input('Sears Credit Card:'))
    worksheet.update_cell(65,4, input('Motorvehicle Insurance:'))
    worksheet.update_cell(70,4, '=sum(D65:D68)') #Total Current Liabilities
    worksheet.update_cell(65,4, input('Honda Shadow Loan:'))
    worksheet.update_cell(70,4, '=sum(D74:D75') #Total Long Term Liabilities
    worksheet.update_cell(70,4, '=D70+D77')  #Total Liabilities



    #Equity Calculations
    worksheet.update_cell(81,4, '=D60-D79') #Equity
    worksheet.update_cell(70,4, '=D79+D81') #Liabilities + Equity
    worksheet.update_cell(85,1, input('Were there any notable events? :'))





    #Asset text
    worksheet.update_cell(2,1, 'Current Assets:')
    worksheet.update_cell(3,1, 'Cash Assets:')
    worksheet.update_cell(2,5, 'Change from Last Month')
    worksheet.update_cell(4,3, 'Cash on Hand:')
    worksheet.update_cell(5,3, 'ACU Account Ending 2188:')
    worksheet.update_cell(6,3, "ACU Account Ending 3393:")
    worksheet.update_cell(7,3, 'ACU Account Ending 1005:')
    worksheet.update_cell(8,3, 'DCU Account Ending 7395:')
    worksheet.update_cell(9,3, 'Ally Account Ending 7105:')
    worksheet.update_cell(10,3,'Ally Account Ending 7713:')
    worksheet.update_cell(13,3, 'Total Cash Assets:') #####
    worksheet.update_cell(15,1, 'Accounts Receivable:')
    worksheet.update_cell(21,3, 'Total Accounts Receivable:')
    worksheet.update_cell(23,1, 'Physical Assets:')
    worksheet.update_cell(32,3, 'Total Physical Assets:')
    worksheet.update_cell(34,1, 'Businesses:')
    worksheet.update_cell(37,3, 'Total Business Assets:')
    worksheet.update_cell(39,1, 'Total Current Assets:')
    worksheet.update_cell(41,1, 'Long Term Assets')
    worksheet.update_cell(43,1, 'Investments:')
    worksheet.update_cell(49,3, 'Total Investments:')
    worksheet.update_cell(51,1, 'Collections:')
    worksheet.update_cell(56,3, 'Total Collections:')
    worksheet.update_cell(58,1, 'Total Long Term Assets:')
    worksheet.update_cell(60,1, 'Total Assets:')

    #Liability text
    worksheet.update_cell(62,1, 'Liabilities:')
    worksheet.update_cell(64,1, 'Current Liabilities:')
    worksheet.update_cell(64,1, 'Honda Shadow Loan:')

    worksheet.update_cell(70,3, 'Total Current Liabilities:')
    worksheet.update_cell(73,1, 'Long Term Liabilities:')
    worksheet.update_cell(77,3, 'Total Long Term Liabilities:')
    worksheet.update_cell(79,1, 'Total Liabilities:')

    #Equity Text
    worksheet.update_cell(81,1, 'Equity:')
    worksheet.update_cell(83,1, 'Liabilities + Equity:')
    worksheet.update_cell(84,1, 'Notable Events:')









    print('Spreadsheet updated')