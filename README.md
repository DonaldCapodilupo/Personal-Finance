# Personal-Finance
Personal equity tracker

This program sets a user up to track their assets, liabilities, income and expenses.

When the program is started, the program starts by making a series of folders and databases. 

Located within the Databases folder, the program creates a 6 separate databases, one for each of the following:
Current Assets, Current liabilities, NonCurrent Assets, NonCurrent Liabilities, Income and Expenses.

The program launches to a main menu where the user can select from the following options:
Update Account Balances, Add an Account, Remove an Account, View Balances and Exit

If the user chooses to Update their Account Balances, they will be brought to a screen that pulls information from the 
"Current Asset", "NonCurrent Asset", "Current Liabilities" and "NonCurrent Liabilities" databases and iterate through 
every account name, prompting the user to enter the current account balance. The database will then update the 
appropriate account with the new account balance. 

If the user decides that they want to Add an Account, they will be brought to a screen where they will be given the 
choice of adding an Asset, a Liability, Income or Expense.

If the user choose Asset or Liability, they will be prompted to chose an option that determins if the account will be 
closed before the end of the year. If the user chooses Income or Expense, these accounts always get closed out at the 
end of the year so this option will be skipped.

After the user specifies Current, NonCurrent, Income or Expense, they will be prompted to decide which specific account
type they would like. Two forms will also appear that allows the user to enter in the account name and the account 
balance. When the user hits the final submit button, the values from the "Generic Account Type", "Account Term" and 
"Specific Account Type" radio buttons, as well as the information typed into the forms input from the user, will be
input into the appropriate account Database.

If the user decides that they want to remove an account, the user will be brought to a page that asks them what account
type they want to remove an account from. When the user selects a primary account type, all of the databases associated 
with that account type will have their account name displayed on the screen next to a button that, when pressed, allows
the user to delete the account from the database. When the user is done, they can click the button to go back to the 
main menu.

If the user decides that they want to View Balances, they will be brought to a screen that displays a balance sheet and
Income Statement utilizing the information found inside of all of the databases. 