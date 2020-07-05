completeBalanceSheet = {"Assets":{"Current_Assets":["Cash","Cash_Equivalent_Bank_Accounts", "Short_Term_Investments",
                                                    "Net_Receivables","Inventory", "Other_Current_Assets"],
                                  "NonCurrent_Assets":["Property_Plant_and_Equipment", "Accumulated_Depreciation",
                                                        "Equity_and_Other_Investments","Goodwill", "Intangible_Assets",
                                                        "Other_Long_Term_Assets"]},
                        "Liabilities":{"Current_Liabilities":["Total_Revenue", "Accounts_Payable", "Taxes_Payable",
                                                              "Accrued_Liabilities", "Deferred_Revenues",
                                                              "Other_Current_Liabilities"],
                                       "NonCurrent_Liabilities":["Long_Term_Debt", "Deferred_Taxes_Liabilities",
                                                                  "Deferred_Revenues","Other_Long_Term_Liabilities"]},
                        "Equity":{"True_Equity":["Common_Stock", "Retained_Earnings", "Accumulated_Other_Comprehensive_Income"]}
                        }



balanceSheetSpecificToGeneral = {
                        "Cash":"Current_Assets",
                       "Cash_Equivalent_Bank_Accounts":"Current_Assets",
                       "Short_Term_Investments":"Current_Assets",
                       "Net_Receivables":"Current_Assets",
                        "Inventory":"Current_Assets",
                       "Other_Current_Assets":"Current_Assets",
                       "Property_Plant_and_Equipment":"NonCurrent_Assets",
                       "Accumulated_Depreciation":"NonCurrent_Assets",
                        "Equity_and_Other_Investments":"NonCurrent_Assets",
                       "Goodwill":"NonCurrent_Assets",
                       "Intangible_Assets":"NonCurrent_Assets",
                       "Other_Long_Term_Assets":"NonCurrent_Assets",
                       "Total_Revenue":"Current_Liabilities" ,
                       "Accounts_Payable":"Current_Liabilities" ,
                       "Taxes_Payable":"Current_Liabilities",
                       "Accrued_Liabilities":"Current_Liabilities",
                        "Other_Current_Liabilities":"Current_Liabilities",
                       "Long_Term_Debt":"NonCurrent_Liabilities",
                       "Deferred_Taxes_Liabilities":"NonCurrent_Liabilities",
                       "Deferred_Revenues":"NonCurrent_Liabilities",
                        "Other_Long_Term_Liabilities":"NonCurrent_Liabilities",

}


