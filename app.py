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
        return render_template('main.html')

@app.route('/UpdateAccountBalances', methods=["POST","GET"])
def update_Accounts():
    if request.method == "POST":
        if request.form['submit_button'] == 'Update Balances':
            from Backend import update_Database_Information

            new_Values = request.form.getlist("New Balances")

            print("Here are the values the user entered to be updated:")
            print(new_Values)

            update_Database_Information(new_Values)

            return redirect(url_for('dashboard'))

        elif request.form['submit_button'] == 'Go Back':
            return redirect(url_for('dashboard'))

    else:
        from Backend import read_Database_Information
        account_Information = read_Database_Information()

        return render_template('UpdateAccounts.html', data=account_Information)

@app.route('/AddAnAccount', methods=["POST","GET"])
def add_Account_To_Database():
    if request.method == "POST":
        if request.form['submit_button'] == 'Upload New Accounts':
            from Backend import create_Database_Row
            user_info = request.form["Upload List"]

            print("This is the information that the user wants to add to the database.")
            print(user_info)

            accounts_to_upload = tuple(request.form["Upload List"].split("\r\n"))
            for account_to_add in accounts_to_upload:
                create_Database_Row(tuple(account_to_add.split(',')))

            return redirect(url_for('dashboard'))
    else:
        return render_template('AddAccount.html')

@app.route('/RemoveAnAccount', methods=["POST","GET"])
def remove_Account_From_Database():
    if request.method == "POST":
        if request.form['submit_button'] == "Remove Item":
            from Backend import delete_Database_Row
            selected = request.form.getlist('checkbox')

            print("These are the accounts that the user wants to remove.")
            print(selected)

            for row in selected:
                delete_Database_Row(row)
            return redirect(url_for('dashboard'))

        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('dashboard'))

    else:
        from Backend import read_Database_Information
        account_Information = read_Database_Information()
        print(account_Information)
        return render_template('RemoveAccounts.html', data=account_Information)



#
if __name__ == '__main__':
    from Backend import programSetup
    programSetup()

    port = 5420
    url = "http://192.168.0.46:{0}".format(port)


    nav.init_app(app)

    app.run(port=port, debug=True, use_reloader=False)