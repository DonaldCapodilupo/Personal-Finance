import os, sqlite3,datetime


def previous_quarter(ref):
    if ref.month < 4:
        return datetime.date(ref.year - 1, 12, 31)
    elif ref.month < 7:
        return datetime.date(ref.year, 3, 31)
    elif ref.month < 10:
        return datetime.date(ref.year, 6, 30)
    return datetime.date(ref.year, 9, 30)


# {'Current_Asset.db': [(4, '2020-12-31', 'Tits', '2555.32'), (1, '2020-03-31', 'Action Figure', '20.00')],}
def get_Database_Values():
    os.chdir('Databases')

    end_Of_Year = str(datetime.date.today())[0:2] + str(int(str(datetime.date.today())[2:4]) - 1) + '-12-31'
    previous_Quarter = str(previous_quarter(datetime.date.today()))

    return_Dict = {"Current_Asset.db": [],
                   "NonCurrent_Asset.db": [],
                   "Current_Liability.db": [],
                   "NonCurrent_Liability.db": []}

    for database in os.listdir(os.getcwd()):
        if database in return_Dict.keys():
            conn = sqlite3.connect(database)
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            available_Tables = (c.fetchall())
            for table in available_Tables:
                table = table[0]
                c.execute("SELECT * FROM  " + table + " ORDER BY Date")
                available_Rows = (c.fetchall())
                for row in available_Rows:
                    the_Date = row[1]
                    if the_Date == end_Of_Year or the_Date == previous_Quarter:
                        return_Dict[database].append(row)
    os.chdir('..')
    print(return_Dict)
    return return_Dict





# {'Current_Asset.db': [(4, '2020-12-31', 'Tits', '2555.32'), (1, '2020-03-31', 'Action Figure', '20.00')],}
def table_Of_Values(dict_Values):


    end_Of_Year = str(datetime.date.today())[0:2] + str(int(str(datetime.date.today())[2:4]) - 1) + '-12-31'
    previous_Quarter = str(previous_quarter(datetime.date.today()))

    return_Dict = {"EOY_Total":0.00,
                   "EOQ_Total":0.00,
                   "Current_Asset.db": 0.00,
                   "NonCurrent_Asset.db": 0.00,
                   "Current_Liability.db": 0.00,
                   "NonCurrent_Liability.db": 0.00}



    for database, list_Of_values in dict_Values.items():
        for db_Row in list_Of_values:
            date = db_Row[1]
            amount = db_Row[3]
            if date == end_Of_Year:
                return_Dict[database] +=  float(amount.replace(",",""))
                return_Dict["EOY_Total"] += float(amount.replace(",",""))
            elif date == previous_Quarter:
                return_Dict[database] +=  float(amount.replace(",",""))
                return_Dict["EOQ_Total"] += float(amount.replace(",",""))
            else:
                print("heyooo")
    print(return_Dict)
    return return_Dict





def table_Of_Changes_In_Values ():
    #Using the values from the other function, create a table
    #YTD $ Change, YTD % Change, QTD $ Change, QTD % Change
    pass


