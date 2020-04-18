
class AccountType:
    def getAccountType_Major(self):
        accountTypes_Major = []
        for i in completeBalanceSheet.keys():
            accountTypes_Major.append(i)
        return listDisplay(accountTypes_Major)
    # Prompts the user to choose short or long term. Equity will need to be adjusted for later
    def getTerm(self, accountTypeMajor):
        account_terms = []
        for i in completeBalanceSheet[accountTypeMajor]:
            account_terms.append(i)
        return listDisplay(account_terms)
    # Using the Major account Type (ex. Asset) and a term (ex. Current Assets), promts the user to pick a specific account type.
    def getAccountType_Minor(self, majorAccountType, term):
        accountTypes_Minor = []
        for i in completeBalanceSheet[majorAccountType][term]:
            accountTypes_Minor.append(i)
        return listDisplay(accountTypes_Minor)
    def main(self):
        accountTypeMajor = getAccountType_Major()  # Asset/Liability/Equity
        term = getTerm(accountTypeMajor)  # Short-term, Long-Term
        specificAccountType = getAccountType_Minor(accountTypeMajor, term)  # The specific short term, asset.
        return specificAccountType
 





