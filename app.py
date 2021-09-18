from flask import Flask, render_template, request,url_for,redirect
from flask_nav import Nav
from flask_nav.elements import Navbar, View

app = Flask(__name__)
nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'mysite',
        View('Dashboard', 'dashboard'),
        View('Add An Account', 'add_Account_To_Database'),
        View('Remove An Account', 'remove_Account_From_Database'),
        View('Update Account Balances', 'update_Accounts'),
    )



@app.route('/', methods=["POST","GET"])
def dashboard():
    if request.method == "GET":
        from Backend import create_Balance_Sheet_HTML, create_Account_Balances_HTML_Table, get_Account_Percentages





        headers = ('Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug')

        hardcoded_Data = {
            "Current Assets":(813.08,1194.3,783.9,3489.03,2866.52,1998.79,1386.07,1795.42,1136.83),
            "NonCurrent Assets": (22619.05,22876.03,23686.49,22583.09,25248.03,26976.007,27919.84,29305.22,30706.34),
            "Current Liabilities": (1497.52,1085.33,1762.72,73.12,62.77,196.64,188.68,862.49,93.64),
            "NonCurrent Liabilities": (0,0,0,0,0,0,0,0,0),
            "Equity":(23420.6,22985,22707.67,25999,28051.78,28778.157,29117.23,30238.15,31749.53)
        }

        #turn accounts column from 550000 into "$5,500.00"


        create_Balance_Sheet_HTML()
        create_Account_Balances_HTML_Table()
        get_Account_Percentages()









        return render_template('main.html',
                               heads=headers,
                               data = hardcoded_Data)

@app.route('/UpdateAccountBalances', methods=["POST","GET"])
def update_Accounts():
    if request.method == "POST":
        if request.form['submit_button'] == 'Update Balances':
            from Backend import read_Database, update_Database_Information

            old_Values = read_Database("Account_Balances.db","Accounts")

            new_Values = request.form.getlist("new_Balances")

            new_Dataframe = old_Values.assign(Value=new_Values)

            update_Database_Information("Account_Balances.db", new_Dataframe, True)
            update_Database_Information("Backup_Balances.db", new_Dataframe, False)

            return redirect(url_for('dashboard'))

        elif request.form['submit_button'] == 'Go Back':
            return redirect(url_for('dashboard'))

    else:
        from Backend import read_Database
        account_Information = read_Database("Account_Balances.db", "Accounts")

        return render_template('UpdateAccounts.html', data=account_Information)

@app.route('/AddAnAccount', methods=["POST","GET"])
def add_Account_To_Database():
    if request.method == "POST":
        if request.form['submit_button'] == 'Add New Account':
            from Backend import create_Database_Row
            import datetime

            scrub_Comma = request.form['account_Balance'].replace(",","")
            clean_Data = float(scrub_Comma.replace("$",""))




            create_Database_Row("Account_Balances.db","Accounts",(str(datetime.date.today()),
                                                                  request.form['account_Type'],
                                                                  request.form['account_Name'],
                                                                  clean_Data,
                                                                  )
                                )
            create_Database_Row("Backup_Accounts.db", "Accounts", (str(datetime.date.today()),
                                                                    request.form['account_Type'],
                                                                    request.form['account_Name'],
                                                                    clean_Data,
                                                                    )
                                )


                


            return redirect(url_for('dashboard'))
    else:
        return render_template('AddAccount.html')

@app.route('/RemoveAnAccount', methods=["POST","GET"])
def remove_Account_From_Database():
    if request.method == "POST":
        if request.form['submit_button'] == "Remove Item":
            from Backend import delete_Database_Row
            selected = request.form.getlist('checkbox')

            for row in selected:
                delete_Database_Row("Account_Balances.db","Accounts",row)

            return redirect(url_for('dashboard'))

        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('dashboard'))

    else:
        from Backend import read_Database
        account_Information = read_Database("Account_Balances.db","Accounts")
        return render_template('RemoveAccounts.html', data=account_Information)




if __name__ == '__main__':
    import random, threading, webbrowser
    from Backend import programSetup
    programSetup(("Databases",),("Account_Balances.db","Backup_Accounts.db", 'Backup_Balances.db'),("Accounts",))

    port = 5420
    url = "http://127.0.0.1:{0}".format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    nav.init_app(app)

    app.run(port=port, debug=True, use_reloader=False)