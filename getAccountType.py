#The purpose of this script is to have specific account types to add/remove rows.

#They dictionary should also be used to set up tables for the initialSetup()
#Have a database for Asset/Liability/Equity
#Have a table for "Cash and Cash Equivalents", "Short Term Investments" etc.

#because listDisplay() returns Ex. "Inventory", need a way to connect it to the Database name.
from Dictionaries.PFinanceDicts import completeBalanceSheet

#Simply used to convert lists into a display the user can choose from
def listDisplay(acceptableChoices):

    print("Which option would you like to choose")
    s = 1   #This is the counter
    for i in acceptableChoices: #Loop through the menu options
        print(str(s) + ") " +i) #Display all of the items in the list as a menu
        s += 1

    userChoice = int(input(">")) #Prompt the user to enter a number

    # Reruns the prompt if the user enters a number that is to big
    while userChoice > len(acceptableChoices):
        print("Invalid data. Please enter a valid number")
        print()
        print("Which option would you like to choose")
        s = 1  # This is the counter
        for i in acceptableChoices:  # Loop through the menu options
            print(str(s) + ") " + i)  # Display all of the items in the list as a menu
            s += 1
        userChoice = int(input(">"))

    #Closes the program if the user selects "Exit"
    #At some point I would like it to step back one function
    if userChoice == (s-1) and acceptableChoices[-1] == "Exit":
        print("Exiting")
        exit()

    #Converts the users numerical entry into the string version of the option selected.
    userChoiceFINAL = acceptableChoices[(int(userChoice)-1)]

    #Return the variable
    return userChoiceFINAL

#Prompts the user to decide between , Asset, Liability or Equity
def getAccountType_Major():
    accountTypes_Major = []
    for i in completeBalanceSheet.keys():
        accountTypes_Major.append(i)
    return listDisplay(accountTypes_Major)

#Prompts the user to choose short or long term. Equity will need to be adjusted for later
def getTerm(accountTypeMajor):
    account_terms = []
    for i in completeBalanceSheet[accountTypeMajor]:
        account_terms.append(i)
    return listDisplay(account_terms)

#Using the Major account Type (ex. Asset) and a term (ex. Current Assets), promts the user to pick a specific account type.
def getAccountType_Minor(majorAccountType, term):
    accountTypes_Minor = []
    for i in completeBalanceSheet[majorAccountType][term]:
        accountTypes_Minor.append(i)
    return listDisplay(accountTypes_Minor)

def main():
    accountTypeMajor = getAccountType_Major() #Asset/Liability/Equity
    term = getTerm(accountTypeMajor) #Short-term, Long-Term
    specificAccountType = getAccountType_Minor(accountTypeMajor, term) #The specific short term, asset.
    return specificAccountType

if __name__ == '__main__':
    main()






