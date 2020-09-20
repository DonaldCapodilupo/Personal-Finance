class SetupTool:
    def __init__(self):
        self.neededDirectories = ['Historical Data', 'Databases']
        self.databaseNames = ["Current_Assets", "NonCurrent_Assets", "Current_Liabilities", "NonCurrent_Liabilities",
                              "Current_Incomes", "Current_Expenses"]
        self.directorySetup()
        self.databaseSetup()

    def directorySetup(self):  # This will ensure that all required files and directories are present before continuing.
        import os
        print("Initializing setup.\n")
        # Create directories
        for directory in self.neededDirectories:
            try:
                # Create target Directory
                os.mkdir(directory)
                print("Directory " + directory + " Created ")
            except FileExistsError:
                print("Directory " + directory + " already exists")
        print("All directories are present.\n")

    def databaseSetup(self):
        import os
        import sqlite3
        os.chdir(os.getcwd()+"/Databases")

        def insertDatabaseTables(cursor, i):
            for s in i:
                try:
                    cursor.execute("CREATE TABLE  " + s + "(ID INTEGER PRIMARY KEY, "
                                                     "Date TEXT, "
                                                     "Description TEXT,"
                                                     "Value TEXT)")
                    print("Creating the Database table:  " + s)
                except sqlite3.OperationalError:
                    print("The table  " + s + " is already present and does not need to be created.")

        from Dictionaries.PFinanceDicts import completeBalanceSheet
        for nameOfDatabase in self.databaseNames:
            conn = sqlite3.connect(nameOfDatabase + '.db')
            c = conn.cursor()
            if nameOfDatabase == "Current_Assets" or nameOfDatabase == "NonCurrent_Assets":
                insertDatabaseTables(c, completeBalanceSheet["Assets"][nameOfDatabase])
            elif nameOfDatabase == "Current_Liabilities" or nameOfDatabase == "NonCurrent_Liabilities":
                insertDatabaseTables(c, completeBalanceSheet["Liabilities"][nameOfDatabase])
            elif nameOfDatabase == "Current_Incomes":
                insertDatabaseTables(c, completeBalanceSheet["Income"]["Current_Incomes"])
            else:
                insertDatabaseTables(c, completeBalanceSheet["Expenses"]["Current_Expenses"])



        print("The database is set up properly.\n")
