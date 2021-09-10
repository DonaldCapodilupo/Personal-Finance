from flask import Flask, render_template, request,url_for,redirect

app = Flask(__name__)





@app.route('/', methods=["POST","GET"])
def main_Menu():
    if request.method == "POST":
        if request.form['btn'] == 'Update Account Balances':
            return redirect(url_for('update_Accounts'))
        if request.form['btn'] == 'Add an Account':
            return redirect(url_for('add_Account_To_Database'))
        if request.form['btn'] == 'Remove an Account':
            return redirect(url_for('remove_Account_From_Database'))
        if request.form['btn'] == 'View Account Balances':
            return redirect(url_for('view_Balances'))
    else:
        return render_template('main.html')

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

            return redirect(url_for('main_Menu'))

        elif request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Menu'))

    else:
        from Backend import read_Database
        account_Information = read_Database("Account_Balances.db", "Accounts")

        return render_template('UpdateAccounts.html', data=account_Information)

@app.route('/AddAnAccount', methods=["POST","GET"])
def add_Account_To_Database():
    if request.method == "POST":
        if request.form['submit_button'] == 'Add New Account':
            from Backend import create_Database_Row, prior_Report_Dates
            import datetime



            create_Database_Row("Account_Balances.db","Accounts",(str(datetime.date.today()),
                                                                  request.form['account_Type'],
                                                                  request.form['account_Name'],
                                                                  request.form['account_Balance'],
                                                                  )
                                )
            create_Database_Row("Backup_Accounts.db", "Accounts", (str(datetime.date.today()),
                                                                    request.form['account_Type'],
                                                                    request.form['account_Name'],
                                                                    request.form['account_Balance'],
                                                                    )
                                )


                


            return redirect(url_for('main_Menu'))
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

            return redirect(url_for('main_Menu'))

        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Menu'))

    else:
        from Backend import read_Database
        account_Information = read_Database("Account_Balances.db","Accounts")
        return render_template('RemoveAccounts.html', data=account_Information)

@app.route('/ViewAccountBalances', methods=["POST","GET"])
def view_Balances():
    if request.method == "POST":
        if request.form['btn_Go_Back'] == 'Go Back':
            return redirect(url_for('main_Menu'))
    else:
        from Backend import read_Database

        print(list(read_Database("Account_Balances.db","Accounts")))
        dataframe = read_Database("Account_Balances.db","Accounts")

        html = dataframe.to_html(classes=["table-bordered", "table-striped", "table-hover"])

        text_file = open("templates/index.html", "w")
        text_file.write(html)
        text_file.close()


        return render_template('ViewBalances.html', data = dataframe,
                               column_Names=list(read_Database("Account_Balances.db","Accounts")),
                               current_Balances_Table=html)




if __name__ == '__main__':
    import random, threading, webbrowser
    from Backend import programSetup
    programSetup(("Databases",),("Account_Balances.db","Backup_Accounts.db", 'Backup_Balances.db'),("Accounts",))

    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    app.run(port=port, debug=False)