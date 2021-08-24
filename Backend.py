import sqlite3, datetime, os


def programSetup(directories:tuple, databases:tuple,tables:tuple):
    import os
    import sqlite3

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
    import os
    import sqlite3
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    tuple_To_Database_Syntax = "?, " * (len(tuple_Of_Values_To_Add)-1)

    c.execute("INSERT INTO "+table+" VALUES (NULL,"+tuple_To_Database_Syntax +"?)",tuple_Of_Values_To_Add)
    os.chdir('..')
    conn.commit()

def read_Database(database, table):
    import pandas as pd
    import sqlite3, os

    os.chdir("Databases")

    con = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * from "+ table, con)
    con.close()
    os.chdir("..")
    return df

def update_Database_Information(database, dataframe):
    import os
    import sqlite3
    os.chdir("Databases")

    conn = sqlite3.connect(database)

    dataframe.to_sql('Accounts', con=conn, if_exists='replace', index=False)

    os.chdir('..')
    conn.commit()

def delete_Database_Row(database, table, value_To_Remove):
    import os
    import sqlite3
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE FROM "+ table +" where Account_Name = ?", [value_To_Remove])
    os.chdir('..')
    conn.commit()
