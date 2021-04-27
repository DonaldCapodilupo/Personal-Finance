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

    today = str(datetime.date.today())
    end_Of_Year = today[0:2] + str(int(today[2:4]) - 1) + '-12-31'
    previous_Quarter = str(previous_quarter(datetime.date.today()))

    return_Dict = {"Current_Asset.db":{"EOY":0.00,
                                       "EOQ":0.00,
                                       "Current":0.00},
                   "NonCurrent_Asset.db":{"EOY":0.00,
                                       "EOQ":0.00,
                                       "Current":0.00},
                   "Current_Liability.db": {"EOY":0.00,
                                       "EOQ":0.00,
                                       "Current":0.00},
                   "NonCurrent_Liability.db":{"EOY":0.00,
                                       "EOQ":0.00,
                                       "Current":0.00},
                   "Equity":{"EOY":0.00,
                            "EOQ":0.00,
                            "Current":0.00}
                   }




    os.chdir('Databases')

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
                    if the_Date == end_Of_Year:
                        return_Dict[database]["EOY"] += float(row[3].replace(",",""))
                    elif the_Date == previous_Quarter:
                        return_Dict[database]["EOQ"] += float(row[3].replace(",",""))
                    elif the_Date == today:
                        return_Dict[database]["Current"] += float(row[3].replace(",",""))
                    else:
                        print(row)
                        print('Whas not a date we care about today')







    try:
        return_Dict["Equity"]["EOY"] = ((return_Dict["Current_Asset.db"]["EOY"] + return_Dict["NonCurrent_Asset.db"]["EOY"])-
        (return_Dict["Current_Liability.db"]["EOY"] + return_Dict["NonCurrent_Liability.db"]["EOY"]))
    except ZeroDivisionError:
        return_Dict["Equity"]["EOY"] = (
                    (return_Dict["Current_Asset.db"]["EOY"] + return_Dict["NonCurrent_Asset.db"]["EOY"]) /1)

    try:
        return_Dict["Equity"]["EOQ"] = (
                    (return_Dict["Current_Asset.db"]["EOQ"] + return_Dict["NonCurrent_Asset.db"]["EOQ"]) -
                    (return_Dict["Current_Liability.db"]["EOQ"] + return_Dict["NonCurrent_Liability.db"]["EOQ"]))
    except ZeroDivisionError:
        return_Dict["Equity"]["EOQ"] = (return_Dict["Current_Asset.db"]["EOQ"] + return_Dict["NonCurrent_Asset.db"][
                                               "EOQ"])/1

    try:
        return_Dict["Equity"]["Current"] = (
                    (return_Dict["Current_Asset.db"]["Current"] + return_Dict["NonCurrent_Asset.db"]["Current"]) -
                    (return_Dict["Current_Liability.db"]["Current"] + return_Dict["NonCurrent_Liability.db"]["Current"]))
    except ZeroDivisionError:
        return_Dict["Equity"]["Current"] = (
                (return_Dict["Current_Asset.db"]["Current"] + return_Dict["NonCurrent_Asset.db"]["Current"]) /1)

    os.chdir('..')
    return return_Dict





# {'Current_Asset.db': [(4, '2020-12-31', 'Tits', '2555.32'), (1, '2020-03-31', 'Action Figure', '20.00')],}
def table_Of_Values():
    import pandas as pd
    df = pd.DataFrame(get_Database_Values())
    result = df.to_html()
    os.chdir('templates')
    text_file = open("table_Of_Values.html", "w")
    text_file.write(result)
    text_file.close()
    os.chdir('..')





def table_Of_Changes_In_Values ():
    today = str(datetime.date.today())
    end_Of_Year = today[0:2] + str(int(today[2:4]) - 1) + '-12-31'
    previous_Quarter = str(previous_quarter(datetime.date.today()))

    return_Dict_B = {"EOY": {"Current Asset": 0.00,
                            "NonCurrent Asset": 0.00,
                            "Current Liability": 0.00,
                             "NonCurrent Liability":0.00,
                             "Equity":0.00},
                   "EOQ": {"Current Asset": 0.00,
                            "NonCurrent Asset": 0.00,
                            "Current Liability": 0.00,
                             "NonCurrent Liability":0.00,
                             "Equity":0.00},
                   "Current": {"Current Asset": 0.00,
                            "NonCurrent Asset": 0.00,
                            "Current Liability": 0.00,
                             "NonCurrent Liability":0.00,
                             "Equity":0.00},
                   }

    os.chdir('Databases')

    for term in return_Dict_B.keys():
        for database in return_Dict_B[term].keys():
            conn = sqlite3.connect(database.replace(' ','_') + '.db')
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            available_Tables = (c.fetchall())
            for table in available_Tables:
                table = table[0]
                c.execute("SELECT * FROM  " + table + " ORDER BY Date DESC")
                available_Rows = (c.fetchall())
                print(available_Rows)
                for row in available_Rows:
                    the_Date = row[1]
                    if the_Date == end_Of_Year:
                        return_Dict_B["EOY"][database] += float(row[3].replace(",", ""))
                    elif the_Date == previous_Quarter:
                        return_Dict_B["EOQ"][database] += float(row[3].replace(",", ""))

                    else:
                        if 'Asset' in database:
                            return_Dict_B["Current"][database] += float(row[3].replace(",", ""))
                        elif 'Liability' in database:
                            return_Dict_B["Current"][database] -= float(row[3].replace(",", ""))
                        else:
                            print('Wait whut?')
                        return_Dict_B["Current"][database] += float(row[3].replace(",", ""))
    os.chdir('..')

    for key in return_Dict_B.keys():
        for database, value in return_Dict_B[key].items():
            if 'Asset' in database:
                return_Dict_B[key]["Equity"] += value
            elif 'Liability' in database:
                return_Dict_B[key]["Equity"] -= value
            else:
                print('Wait whut?')



    import pandas as pd

    df = pd.DataFrame(return_Dict_B)
    result = df.to_html()
    os.chdir('templates')
    text_file = open("table_Of_Changes_In_Values.html", "w")
    text_file.write(result)
    text_file.close()





    os.chdir('..')
    pass


