# tkinter is used for the user interface
import tkinter as tk
# custom classes made to create good looking buttons and entries
from class_buttons import Button
from class_entry import Entry


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # basic config
        # tk.Tk.wm_geometry(self, '1280x720')
        tk.Tk.wm_resizable(self, False, False)
        tk.Tk.wm_title(self, 'Personal Finance Calculator')   #The title text of every window
        tk.Tk.config(self, bg = '#333333') # hex color #333333 is dark gray
        # create variable
        self.current_frame = None
        # set home frame
        self.switch_frame(MainMenu)

    # this function switches the current frame for the frame entered
    def switch_frame(self, frame):
        try:
            self.current_frame.destroy()
        except:
            pass
        self.current_frame = frame(self)
        self.current_frame.pack()



class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')

        tk.Label(self, text = 'Personal Finance Calculations', font = ('Arial', 25, 'bold'), bg = '#333333', fg = '#ffffff').pack(pady = 30)
        tk.Label(self, bg = '#333333').pack(pady = 25) # spacing

        # using custom buttons for the ui
        update_accounts_button = Button(root = self, text='Update Accounts', command = lambda x: master.switch_frame(UpdateAccounts))
        add_record_button = Button(root = self, text='Add an Account', command = lambda x: master.switch_frame(UpdateAccounts))
        remove_record_button = Button(root = self, text='Remove an Account', command = lambda x: master.switch_frame(UpdateAccounts))
        view_balances_button = Button(root = self, text='View Balances', command = lambda x: master.switch_frame(UpdateAccounts))
        exit_button = Button(root = self, text='Exit', command = lambda x: master.destroy())

        update_accounts_button.pack(pady = 15)
        add_record_button.pack(pady = 15)
        remove_record_button.pack(pady = 15)
        view_balances_button.pack(pady = 15)
        exit_button.pack(pady = 15)


class UpdateAccounts(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')

        self.main_label = tk.Label(self, text='Click the button to start',
                 font=('Arial', 25, 'bold'), bg='#333333', fg='#ffffff')
        tk.Label(self, bg='#333333').pack(pady=25)  # spacing
        self.entry = Entry(self, alt_text='Current previous value was %v ')
        # self.entry_length.pack(pady = 10)
        submit_button = Button(root=self, text='Confirm', command=self.changeLabel)

        self.main_label.pack(pady = 15)
        self.entry.pack(pady = 15)
        submit_button.pack(pady = 15)

    def changeLabel(self):
        self.main_label.config(text="Yay you clicked")
        self.main_label.pack()

    def updateLoop(self,master,item):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg='#333333')
        tk.Label(self, text='What is the current balance of :',
                 font=('Arial', 25, 'bold'), bg='#333333', fg='#ffffff').pack(pady=30)
        tk.Label(self, bg='#333333').pack(pady=25)  # spacing
        self.entry_length = Entry(self, alt_text='Current previous value was %v ').pack(pady=15)
        # self.entry_length.pack(pady = 10)
        Button(root=self, text='Confirm', command=lambda x: self.changeLabel).pack(pady=15)


class EachAccountToUpdate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')
        tk.Label(self, text='What is the current balance of :',
                 font=('Arial', 25, 'bold'), bg='#333333', fg='#ffffff').pack(pady=30)
        tk.Label(self, bg='#333333').pack(pady=25)  # spacing
        self.entry_length = Entry(self, alt_text='Current previous value was %v ').pack(pady=15)
        # self.entry_length.pack(pady = 10)
        Button(root=self, text='Confirm', command=lambda x: master.destroy()).pack(pady=15)










        #self.entry_length = Entry(self, alt_text='Enter password length')
        #self.entry_length.pack(pady = 10)
#
        #self.entry_name = Entry(self, alt_text='Enter your name')
        #self.entry_name.pack(pady = 10)
#
        #self.entry_year = Entry(self, alt_text='Enter your birth year')
        #self.entry_year.pack(pady = 10)
#
        #Button(root = self, text='Confirm', command = lambda x: self.generate_password(int(self.entry_length.get()), self.entry_name.get(), self.entry_year.get())).pack(pady = 15)
#
        #self.entry_password = Entry(self, alt_text='')
        #self.entry_password.pack(pady = 15)
#
        #Button(root = self, text='Copy', command = lambda x: pyperclip.copy(self.entry_password.get())).pack(pady = 15)


    def generate_password(self, length, user_name, birth_year):
        appropriate_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

        generator = PasswordGenerator(passwordLength = length, appropriateCharacters = appropriate_characters)
        password = PasswordGenerator.generateDefaultPassword(generator, userName = user_name, birth_year = birth_year)

        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(tk.END, password)





class FullyRandom(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')







if __name__ == '__main__':
    window = Main()
    window.mainloop()