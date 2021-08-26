import sqlite3, datetime, os


def programSetup(directories:tuple, databases:tuple,tables:tuple):
    for directory in directories:
        try:
            os.mkdir(directory)
            print("Database " + directory + " Created ")
        except FileExistsError:
            print(directory+" directory already exists")

    os.chdir("Databases")

    for database in databases:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        for table_Name in tables:
            try:
                c.execute("CREATE TABLE  " + table_Name + "(ID INTEGER PRIMARY KEY, "
                                                                            "Date TEXT, "
                                                                            "Account_Type TEXT, "
                                                                            "Account_Name TEXT, "
                                                                            "Value TEXT)")
            except sqlite3.OperationalError:
                print(table_Name + " already exists.")

    os.chdir('..')

def create_Database_Row(database, table, tuple_Of_Values_To_Add):
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    tuple_To_Database_Syntax = "?, " * (len(tuple_Of_Values_To_Add)-1)

    c.execute("INSERT INTO "+table+" VALUES (NULL,"+tuple_To_Database_Syntax +"?)",tuple_Of_Values_To_Add)
    os.chdir('..')
    conn.commit()

def read_Database(database, table):
    import pandas as pd

    os.chdir("Databases")

    con = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * from "+ table, con)
    con.close()

    os.chdir("..")
    return df

def update_Database_Information(database, dataframe, replace):
    os.chdir("Databases")

    conn = sqlite3.connect(database)

    if replace:
        dataframe.to_sql('Accounts', con=conn, if_exists='replace', index=False)
    else:
        dataframe.to_sql('Accounts', con=conn, if_exists='append', index_label='id')

    os.chdir('..')
    conn.commit()

def delete_Database_Row(database, table, value_To_Remove):
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE FROM "+ table +" where Account_Name = ?", [value_To_Remove])
    os.chdir('..')
    conn.commit()


def prior_Report_Dates():
    today = str(datetime.date.today())
    end_Of_Year = today[0:2] + str(int(today[2:4]) - 1) + '-12-31'

    ref = datetime.date.today()
    if ref.month < 4:
        return today, end_Of_Year, str(datetime.date(ref.year - 1, 12, 31))
    elif ref.month < 7:
        return today, end_Of_Year, str(datetime.date(ref.year, 3, 31))
    elif ref.month < 10:
        return today, end_Of_Year, str( datetime.date(ref.year, 6, 30))
    return today, end_Of_Year, str(datetime.date(ref.year, 9, 30))




