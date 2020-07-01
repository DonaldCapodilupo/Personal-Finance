class ListDisplay:
    def __init__(self, listToDisplay,addExit=True):
        self.listToDisplay = list(listToDisplay)
        self.addExit = addExit

        self.displayList()

    def validateData(self):
        print("Please select which number you would like.")
        user_input = input(">")
        while not user_input.isnumeric():
            user_input = input("Error: Enter an acceptable number: ")


        while int(user_input) > (len(self.listToDisplay) + 1):
            user_input = input("Error: Enter an acceptable number: ")

        if int(user_input) == (len(self.listToDisplay)+1) and self.addExit:
            exit()

        else:
            userChoiceFINAL = self.listToDisplay[(int(user_input) - 1)]
            print(userChoiceFINAL)
            return userChoiceFINAL


    def displayList(self):
        while True:
            print("Which option would you like to choose")
            number = 1  # This is the counter to display in the output string.
            for item in self.listToDisplay:  # Loop through the menu options
                print(str(number) + ") " + item)  # Display all of the items in the list as a menu
                number += 1
            if self.addExit:
                print(str(number) + ") Exit")
                number += 1
            self.validateData()










