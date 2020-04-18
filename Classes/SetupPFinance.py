class SetupTool:
    def directorySetup():  # This will ensure that all required files and directories are present before continuing.
        import os
        print("Initializing setup.\n")
        # Create directories
        neededDirectories = ['Historical Data', 'Databases']
        for i in neededDirectories:
            try:
                # Create target Directory
                os.mkdir(i)
                print("Directory " + i + " Created ")
            except FileExistsError:
                print("Directory " + i + " already exists")
        print("All directories are present.\n")

    def databaseSetup():
        import os
        import sqlite3
        os.chdir(os.getcwd()+"/Databases")
        dataBaseNames = ["Current_Assets", "NonCurrent_Assets", "Current_Liabilities", "NonCurrent_Liabilities"]
        from Dictionaries.PFinanceDicts import completeBalanceSheet

        def insertDatabaseTables(c, i):
            for s in i:
                try:
                    c.execute("CREATE TABLE  " + s + "(ID INTEGER PRIMARY KEY, "
                                                     "Date TEXT, "
                                                     "Description TEXT,"
                                                     "Value TEXT)")
                    print("Creating the Database table:  " + s)
                except sqlite3.OperationalError:
                    print("The table  " + s + " is already present and does not need to be created.")

        for nameOfDatabase in dataBaseNames:

            conn = sqlite3.connect(nameOfDatabase + '.db')
            c = conn.cursor()

            if nameOfDatabase == dataBaseNames[0]:
                insertDatabaseTables(c, completeBalanceSheet["Assets"]["Current Assets"])
            elif nameOfDatabase == dataBaseNames[1]:
                insertDatabaseTables(c, completeBalanceSheet["Assets"]["NonCurrent Assets"])
            elif nameOfDatabase == dataBaseNames[2]:
                insertDatabaseTables(c, completeBalanceSheet["Liabilities"]["Current Liabilities"])
            elif nameOfDatabase == dataBaseNames[3]:
                insertDatabaseTables(c, completeBalanceSheet["Liabilities"]["NonCurrent Liabilities"])



        print("The database is set up properly.\n")
