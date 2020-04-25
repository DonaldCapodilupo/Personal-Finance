class ListDisplay:
    def __init__(self, listToDisplay):
        self.listToDisplay = list(listToDisplay)



    def displayList(self, addExit=True):
        while True:
            print("Which option would you like to choose")
            s = 1  # This is the counter to display in the output string.
            for i in self.listToDisplay:  # Loop through the menu options
                print(str(s) + ") " + i)  # Display all of the items in the list as a menu
                s += 1
            if addExit:
                print(str(s) + ") Exit")
                s += 1
            userChoice = int(input(">"))  # Prompt the user to enter a number
            if userChoice == len(self.listToDisplay) + 1 and addExit:
                exit()
            elif userChoice > len(self.listToDisplay):
                print("Invalid data. Please enter a valid number")
            else:
                userChoiceFINAL = self.listToDisplay[(int(userChoice) - 1)]
                return userChoiceFINAL









