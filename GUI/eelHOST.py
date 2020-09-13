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
    from Classes.AccountClasses import balance_Sheet_Item
    conn = sqlite3.connect("C:\\Users\Don\Documents\Github Folder\Personal-Finance\Databases\Current_Assets.db")
    c = conn.cursor()
    today = str(datetime.date.today())

    newRow = balance_Sheet_Item("No ID needed", description, value)

    # Append the data to the proper table in the database. Confirm for the user. Return to main menu.
    c.execute("INSERT INTO " + specificType + " VALUES (NULL, ?, ?, ?)",
              (today, newRow.accountNickName,
               newRow.accountBalance))  # This line of code added a new row to the database.
    conn.commit()
    print(genericType + " has been added.\n")



eel.init('GUI-EEL')
eel.start('main.html')

