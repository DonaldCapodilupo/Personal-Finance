import eel

#Sample function. Returns the values of the radio buttons from "AddAccounts.html"
@eel.expose
def printRadioButtonValues(genericType, term, specificType, description, value):
    print(genericType)
    print(term)
    print(specificType)
    print(description)
    print(value)

#Need to create a function that will add the item to the Database

@eel.expose
def addAccountToDatabase(genericType, term, specificType, description, value):
    import sqlite3, datetime, os
    conn = sqlite3.connect("C:\\Users\Don\Documents\Github Folder\Personal-Finance\Databases\\" +genericType +".db")
    c = conn.cursor()
    today = str(datetime.date.today())


    # Append the data to the proper table in the database. Confirm for the user. Return to main menu.
    c.execute("INSERT INTO " + specificType + " VALUES (NULL, ?, ?, ?)",
              (today, description,
               value))  # This line of code added a new row to the database.
    conn.commit()
    print(genericType + " has been added.\n")

#from Classes.SetupPFinance import SetupTool
#accountSetup = SetupTool()



eel.init('../GUI-EEL')
eel.start('main.html')

