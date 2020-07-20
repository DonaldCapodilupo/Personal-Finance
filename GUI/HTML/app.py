import eel
from Classes.DatabaseRetrieval import DatabaseManipulation


eel.init('web')
eel.start('main.html', block=False)


@eel.expose
def send(accountName, accountValue,primaryAccountType):
    print("Account Name: " + accountName)
    print("Account Balance: " + accountValue)
    print(primaryAccountType)
    return "ok"

while True:
    text = eel.readTextBox()()
    value = eel.readValueBox()()
    #radioButtons = eel.displayRadioValue()()
    print("Text box contents: {}".format(text))
    print("Value box contents: {}".format(value))
    eel.sleep(2.0)
    #print("Radio button contents: {}".format(radioButtons))
    eel.sleep(2.0)



