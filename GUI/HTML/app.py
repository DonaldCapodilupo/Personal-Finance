import eel


eel.init('web')



@eel.expose
def my_python_method(parm1,parm2):
    print(parm1+parm2)

eel.start('main.html')