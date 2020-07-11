class ListDisplay:
    def __init__(self, listToDisplay,addExit=True, addGoBack=True):
        self.listToDisplay = listToDisplay
        self.addExit = addExit
        self.addGoBack = addGoBack
        self.userChoice = ""

    def displayList(self):
        print("Which option would you like to choose")
        additionalOptionNumbers = 0
        for number, item in enumerate(self.listToDisplay,start=1):
            print(str(number) + ") " + item)  # Display all of the items in the list as a menu
            number += 1
            additionalOptionNumbers = number
        if self.addGoBack:
            print(str(additionalOptionNumbers) + ") Go Back")
            additionalOptionNumbers += 1
        if self.addExit:
            print(str(additionalOptionNumbers) + ") Exit")
            additionalOptionNumbers += 1

        print("Please select which number you would like.")
        user_input = input(">")

        while not user_input.isnumeric() or (int(user_input)> len(self.listToDisplay) +2):
            print("That is invalid input. Please select a valid number.")
            user_input = input(">")

        if int(user_input) == (len(self.listToDisplay) + 1):
            return False

        if int(user_input) == (len(self.listToDisplay) + 2) and self.addExit:
            exit()
        else:
            return self.listToDisplay[int(user_input) - 1]


#class DictionaryDisplay:
#    def __init__(self, dictionary,addExit=True, addGoBack=True):
#        self.dictionary = dictionary
#        self.addExit = addExit
#        self.addGoBack = addGoBack
#        self.userChoice = ""
#
#    def displayList(self):
#        print("Which option would you like to choose")
#          # This is the counter to display in the output string.
#        for number, item in enumerate(self.dictionary):  # Loop through the menu options
#            print(str(number) + ") " + item)  # Display all of the items in the list as a menu
#            number += 1
#            if self.addGoBack:
#                print(str(number) + ") Go Back")
#                number += 1
#            if self.addExit:
#                print(str(number) + ") Exit")
#                number += 1
#
#        print("Please select which number you would like.")
#        user_input = input(">")
#
#        while not user_input.isnumeric() or (int(user_input)> len(self.listToDisplay) +2):
#            print("That is invalid input. Please select a valid number.")
#            user_input = input(">")
#
#        if int(user_input) == (len(self.listToDisplay) + 1):
#            return False
#
#        if int(user_input) == (len(self.listToDisplay) + 2) and self.addExit:
#            exit()
#        else:
#            return self.listToDisplay[int(user_input) - 1]
##TODO Add to the function to allow for a "Go Back" option.
#
#from Dictionaries.PFinanceDicts import completeBalanceSheet
#dictionary = completeBalanceSheet
#DictionaryDisplay(dictionary)







