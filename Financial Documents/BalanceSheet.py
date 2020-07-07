completeBalanceSheet = {"Assets":{"Current Assets":["Cash","Cash_Equivalent_Bank_Accounts", "Short_Term_Investments",
                                                    "Net_Receivables","Inventory", "Other_Current_Assets"],
                                  "NonCurrent Assets":["Property_Plant_and_Equipment", "Accumulated_Depreciation",
                                                        "Equity_and_Other_Investments","Goodwill", "Intangible_Assets",
                                                        "Other_Long_Term_Assets"]},
                        "Liabilities":{"Current Liabilities":["Total_Revenue", "Accounts_Payable", "Taxes_Payable",
                                                              "Accrued_Liabilities", "Deferred_Revenues",
                                                              "Other_Current_Liabilities"],
                                       "NonCurrent Liabilities":["Long_Term_Debt", "Deferred_Taxes_Liabilities",
                                                                  "Deferred_Revenues","Other_Long_Term_Liabilities"]},
                        "Equity":{"True Equity":["Common_Stock", "Retained_Earnings", "Accumulated_Other Comprehensive_Income"]}
                        }






class BalanceSheetDisplay:
    def __init__(self, Cash, Cash_Equivalent, Short_Term_Investments, Net_Receivables, Inventory, Other_Current_Assets,
                 Property_Plant_and_Equipment, Accumulated_Depreciation, Equity_and_Other_Investments, Goodwill,
                 Intangible_Assets, Other_Long_Term_Assets, Total_Revenue, Accounts_Payable, Taxes_Payable,
                 Accrued_Liabilities, Deferred_Cur_Revenues, Other_Current_Liabilities, Long_Term_Debt,
                 Deferred_Taxes_Liabilities, Deferred_Long_Revenues, Other_Long_Term_Liabilities):

        #Set up all qualities
        self.Cash = Cash
        self.Cash_Equivalent = Cash_Equivalent
        self.Short_Term_Investments = Short_Term_Investments
        self.Net_Receivables = Net_Receivables
        self.Inventory = Inventory
        self.Other_Current_Assets = Other_Current_Assets
        self.CashProperty_Plant_and_Equipment = Property_Plant_and_Equipment
        self.Accumulated_Depreciation = Accumulated_Depreciation
        self.Equity_and_Other_Investments = Equity_and_Other_Investments
        self.Goodwill = Goodwill
        self.Intangible_Assets = Intangible_Assets
        self.Other_Long_Term_Assets = Other_Long_Term_Assets
        self.Total_Revenue = Total_Revenue
        self.Accounts_Payable = Accounts_Payable
        self.Taxes_Payable = Taxes_Payable
        self.Accrued_Liabilities = Accrued_Liabilities
        self.Deferred_Cur_Revenues = Deferred_Cur_Revenues
        self.Other_Current_Liabilities = Other_Current_Liabilities
        self.Long_Term_Debt = Long_Term_Debt
        self.Deferred_Taxes_Liabilities = Deferred_Taxes_Liabilities
        self.Deferred_Long_Revenues = Deferred_Long_Revenues
        self.Other_Long_Term_Liabilities = Other_Long_Term_Liabilities

    def displayBalances(self):
        import pandas as pd
        import sqlite3, os
        os.chdir("/home/doncapodilupo/PycharmProjects/Personal-Finance-master/Databases")

        databasesForBalanceSheet = ["Current_Assets.db", "Current_Liabilities.db","NonCurrent_Assets.db",
                                    "NonCurrent_Liabilities.db"]

        balSheet = []

        for db in databasesForBalanceSheet:
            con = sqlite3.connect(db)
            if db == 'Current_Assets.db':
                for i in completeBalanceSheet["Assets"]["Current Assets"]:
                    df = pd.read_sql_query("SELECT * from "+i, con)
                    if not df.empty:
                        balSheet.append(df.values)

            elif db == 'NonCurrent_Assets.db':
                for i in completeBalanceSheet["Assets"]["NonCurrent Assets"]:
                    df = pd.read_sql_query("SELECT * from " + i, con)
                    if not df.empty:
                        balSheet.append(df.values)
            elif db == 'Current_Liabilities.db':
                for i in completeBalanceSheet["Liabilities"]["Current Liabilities"]:
                    df = pd.read_sql_query("SELECT * from " + i, con)
                    if not df.empty:
                        balSheet.append(df.values)
            elif db == 'NonCurrent_Liabilities.db':
                for i in completeBalanceSheet["Liabilities"]["NonCurrent Liabilities"]:
                    df = pd.read_sql_query("SELECT * from " + i, con)
                    if not df.empty:
                        balSheet.append(df.values)


            # Verify that result of SQL query is stored in the dataframe
        print("|".ljust(5)+"Account Name".center(15)+"|".center(15)+"Name".center(15)+"|".center(15)+"Account Balance".center(15)+
              "|".center(15)+ "Change From Last Month".center(15)+"|".center(15))
        for i in balSheet:
            for s in i:
                print(s[2].center(15)+s[3].center(25))

