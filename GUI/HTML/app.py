import eel
from Classes.DatabaseRetrieval import DatabaseManipulation


eel.init('web')
eel.start('main.html', block=False)


@eel.expose
def send(msg):
    print("Received Message: " + msg)
    return "ok"

while True:
    text = eel.readTextBox()()
    value = eel.readValueBox()()
    #accountType = eel.readRadioButtons()()
    print("Text box contents: {}".format(text))
    eel.sleep(2.0)
    print("Value box contents: {}".format(value))
    eel.sleep(2.0)



