class ListDisplay:
    def __init__(self, listToDisplay,addExit=True):
        self.listToDisplay = listToDisplay
        self.addExit = addExit
        self.userChoice = ""



    def displayList(self):
        print("Which option would you like to choose")
        number = 1  # This is the counter to display in the output string.
        for item in self.listToDisplay:  # Loop through the menu options
            print(str(number) + ") " + item)  # Display all of the items in the list as a menu
            number += 1
        if self.addExit:
            print(str(number) + ") Exit")
            number += 1

        print("Please select which number you would like.")
        user_input = input(">")

        while not user_input.isnumeric() or (int(user_input)> len(self.listToDisplay) +1):
            print("That is invalid input. Please select a valid number.")
            user_input = input(">")

        if int(user_input) == (len(self.listToDisplay) + 1) and self.addExit:
            exit()
        else:
            return self.listToDisplay[int(user_input) - 1]









