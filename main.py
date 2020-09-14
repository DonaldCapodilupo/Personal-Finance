from os import path
import os



#/home/user/Github_Files/Personal-Finance
ROOT = path.dirname(path.realpath(__file__))
print(ROOT)


if __name__ == "__main__":
    import eel

    # Set Up Directories, Set Up Databases
    from Classes.SetupPFinance import SetupTool
    accountSetup = SetupTool()
    os.chdir(ROOT)

    # Sample function. Returns the values of the radio buttons from "AddAccounts.html"
    @eel.expose
    def printRadioButtonValues(genericType, term, specificType, description, value):
        print(genericType)
        print(term)
        print(specificType)
        print(description)
        print(value)


    #Display Data ToWebPage from database






    # Need to create a function that will add the item to the Database

    #Take Data From Web Page and put it in a database.
    @eel.expose
    def addAccountToDatabase(genericType, term, specificType, description, value):
        import sqlite3, datetime, os
        if term is None:
            conn = sqlite3.connect(
                "C:\\Users\Don\Documents\Github Folder\Personal-Finance\Databases\\" + genericType + ".db")
        else:
            conn = sqlite3.connect("C:\\Users\Don\Documents\Github Folder\Personal-Finance\Databases\\" + term + "_" + genericType + "s.db")
        c = conn.cursor()
        today = str(datetime.date.today())

        # Append the data to the proper table in the database. Confirm for the user. Return to main menu.
        if specificType is None:
            specificType = genericType

        c.execute("INSERT INTO " + specificType + " VALUES (NULL, ?, ?, ?)",
                  (today, description,
                   value))  # This line of code added a new row to the database.
        conn.commit()
        print(genericType + " has been added.\n")




    eel.init('GUI-EEL')
    eel.start('main.html')

