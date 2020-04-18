#The most basic entry allowed. All classes will inheret a "account nickname" and an "account balance"
#All account types are accounted for but all need to be reviewed as the last few are not accurate.
completeBalanceSheet = {"Assets":{"Current Assets":["Cash","Cash Equivalent (Bank Accounts)", "Short Term Investments","Net Receivables",
                                                    "Inventory", "Other Current Assets"],
                                  "None Current Assets":["Property, Plant and Equipment", "Accumulated Depreciation", "Equity and Other Investments",
                                                         "Goodwill", "Intangible Assets", "Other Long Term Assets"]},
                        "Liabilities":{"Current Liabilities":["Short Term Debt", "Current Portion of Long Term Debt", "Accounts Payable", "Taxes Payable",
                                                              "Accrued Liabilities", "Deferred Revenues", "Other Current Liabilities"],
                                       "Non-current Liabilities":["Long Term Debt", "Deferred Taxes Liabilities", "Deferred Revenues",
                                                                  "Other Long Term Liabilities"]},
                        "Equity":{"True Equity":["Common Stock", "Retained Earnings", "Accumulated Other Comprehensive Income"]}}

#The foal of this function is to pull values from the classes and determin the montly depreciation amount.
def depreciationAmount(purchasePrice, expectedLife):
    if expectedLife > 10:
        deprAmount = purchasePrice / (expectedLife * expectedLife)
    else:
        deprAmount = purchasePrice / expectedLife
    return deprAmount

####super().__init__ DOES NOT NEED self, ##########
class balance_Sheet_Item:
    def __init__(self, accountID, accountNickName, accountBalance):
        self.accountID = accountID
        self.accountNickName = accountNickName
        self.accountBalance = accountBalance

#Short Term Investments
class cash(balance_Sheet_Item):
    def __init__(self, accountNickName, accountBalance):
        super().__init__(accountNickName,accountBalance)

class cash_Equivalent(balance_Sheet_Item):
    def __init__(self, accountNickname, accountBalance, institution, interestRate):
        super().__init__(accountNickname, accountBalance)
        self.institution = institution
        self.interestRate = interestRate

class short_Term_Investments(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, institution, interestRate, maturityDate):
        super().__init__(accountNickname,accountBalance, institution, interestRate)
        self.maturityDate = maturityDate

class short_Term_Receivables(short_Term_Investments):
    def __init__(self, accountNickname, accountBalance, institution, interestRate, maturityDate, creditor):
        super().__init__(accountNickname, accountBalance, institution, interestRate, maturityDate)
        self.creditor = creditor

class inventory(balance_Sheet_Item):
    def __init__(self, accountNickname, salesValue, COGS, vendor, staleDate, merchant):
        super().__init__(accountNickname, accountBalance=salesValue)
        self.COGS = COGS
        self.vendor = vendor
        self.staleDate = staleDate
        self.merchant = merchant

class other_Current_assets(balance_Sheet_Item):
    def __init__(self, accountNickname, accountBalance, description):
        super().__init__(accountNickname, accountBalance)
        self.description = description

#Long-Term Investments
class property_Plant_Equipment:
    def __init__(self, purchasePrice, expectedLife, salvageValue):
        self.purchasePrice = purchasePrice
        self.expectedLife = expectedLife
        self.salvageValue = salvageValue

class accumulated_Depreciation(balance_Sheet_Item):
    def __init__(self, accountNickname, accountBalance):
        super().__init__(accountNickname, accountBalance)
    def sumDepreciation(self):
        pass#One day, this function will be able to "sumif" a database column and return the running deprciation total. (if name = car, sum deprAmt)

class equity_Other_Investments(balance_Sheet_Item):
    def __init__(self, accountNickname, accountBalance, investmentType, companyName):
        super().__init__(accountNickname, accountBalance)
        self.investmentType = investmentType
        self.companyName = companyName

class goodwill(other_Current_assets):
    def __init__(self, accountNickname, accountBalance, description):
        super().__init__(accountNickname, accountBalance, description)

class intangible_Assets(other_Current_assets):
    def __init__(self, accountNickname,accountBalance, description, assetType):
        super().__init__(accountNickname, accountBalance, description)
        self.assetType = assetType #Patent, copyright etc.

class other_Long_Term_Assets(other_Current_assets):
    def __init__(self, accountNickname, accountBalance, description):
        super().__init__(accountNickname, accountBalance, description)

#Short Term Liabilities
class short_Term_Debt(cash_Equivalent):                    #Current liabilities are listed on the balance sheet under the liabilities section and are paid from the revenue generated from the operating activities of a company.
    def __init__(self, accountNickname, accountBalance, interestRate, institution, debtReason):
        super().__init__(accountNickname, accountBalance, interestRate, institution)
        self.debtReason = debtReason

class current_Long_Term_Debt(short_Term_Debt):                    #Current liabilities are listed on the balance sheet under the liabilities section and are paid from the revenue generated from the operating activities of a company.
    def __init__(self, accountNickname, accountBalance,interestRate, institution, debtReason):
        super().__init__(accountNickname, accountBalance, interestRate, institution, debtReason)

class accounts_Payable(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class taxes_Payable(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class accrued_Liabilities(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class deferred_Revenues(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class other_Current_Liabilities(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

#Long Term Liabilities
class long_Term_Debt(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class deferred_Taxes_Liabilities(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class other_Long_Term_Liabilities(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

#Equity
class common_Stock(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class retained_Earnings(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)

class accumulated_Other_Comprehensive_Income(cash_Equivalent):
    def __init__(self, accountNickname, accountBalance, interestRate, institution):
        super().__init__(accountNickname, accountBalance, interestRate, institution)
