

financialInstitutions = {
    "Athol Credit Union":"Snapshot Financials - Close Soonish",
    "Ally Bank":"Close two joint accounts",
    "Vanguard":"Convert to IRA",
    "TD Bank":"Close, try to avoid fee?",
    "DCU":"Keep. Have emergency $1000 in there",
}




class Stock:
    def __init__(self, institution, symbol, purchasePrice, description, longTerm=True):
        self.institution = str(institution)
        self.symbol = str(symbol)
        self.purchasePrice = str(purchasePrice)
        self.description = str(description)

    def updateStockValue(self):
        #Use an API or a scraper to update current stock prices
        pass

    def getInstitution(self):
        return self.institution
    def getSymbol(self):
        return self.symbol
    def getPurchasePrice(self):
        return self.purchasePrice
    def getDescription(self):
        return self.description

class FinancialInstitution:
    def __init__(self, institution, nickname, interestRate, checking=True):
        self.institution = str(institution)
        self.nickname = str(nickname)
        self.interestRate = str(interestRate) + "%"
    def getInstitution(self):
        return self.institution
    def getNickname(self):
        return self.nickname
    def getInterestRate(self):
        return self.interestRate

creditCards = {
    "Chase Preferred":"Keep, use until fee no longer becomes worth it.",
    "TD Bank":"Set up recurring transaction so that it gets used.",
    "JC Penny":"Set up recurring transaction so that it gets used.",
    "Amazon":"Pay off, use for Amazon purchases. Get limit raised in a few months.",
    "Chase Freedom":"Only keep in wallet in case you need to do chores",
    ""
}

class CreditCard:
    def __init__(self, institution, nickname, interestRate, fee=False):
        self.institution = str(institution)
        self.nickname = str(nickname)
        self.interestRate = str(interestRate) +"%"




    def getInstitution(self):
        return self.institution
    def getNickname(self):
        return self.nickname
    def getInterestRate(self):
        return self.interestRate
