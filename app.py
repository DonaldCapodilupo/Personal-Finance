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
        if request.form['btn_Go_Back'] == 'Go Back':
            from Backend import update_Account_Balances, completeBalanceSheet
            import copy
            user_Input = request.form.to_dict()


            update_Dict = copy.deepcopy(completeBalanceSheet)


            for key, value in user_Input.items():
                account_Information = tuple(map(str, key.split(',')))
                if len(account_Information) > 1:
                    #{'Asset': {'Current Asset': {'Cash': {'Wallet Cash': '1 mill', 'Spare Change': '0.35'}, 'Cash Equivalent Bank Accounts': {'Bank Acct': '100.00', 'Chase Bank': '1000'} } } }
                    update_Dict[account_Information[0]][account_Information[1]][account_Information[2]][account_Information[3]] = value
            update_Account_Balances(update_Dict)


            return redirect(url_for('main_Menu'))
    else:
        from Backend import get_Current_Balance_Information_From_Database
        balances = get_Current_Balance_Information_From_Database()
        print(balances)
        return render_template('UpdateAccounts.html', data=balances)

@app.route('/AddAnAccount', methods=["POST","GET"])
def add_Account_To_Database():
    if request.method == "POST":
        if request.form['btn'] == 'Update Account Balances':
            from Backend import add_Account_To_Database
            add_Account_To_Database(request.form['AccountTerm'], request.form['PrimaryAccountType'],request.form['accountName'],
                        request.form['accountBalance'], request.form['Final_Account_Type'])
            return redirect(url_for('main_Menu'))
    else:
        return render_template('AddAccount.html')

@app.route('/RemoveAnAccount', methods=["POST","GET"])
def remove_Account_From_Database():
    if request.method == "POST":
        if request.form['btn_Go_Back'] == 'Go Back':
            from Backend import remove_Account_From_Database
            selected = request.form.getlist('SpecificAccount')
            print(selected)
            for row in selected:
                remove_Account_From_Database(row)


            return redirect(url_for('main_Menu'))

    else:
        from Backend import get_Current_Balance_Information_From_Database
        account_Information = get_Current_Balance_Information_From_Database()
        return render_template('RemoveAccounts.html', data=account_Information)

@app.route('/ViewAccountBalances', methods=["POST","GET"])
def view_Balances():
    if request.method == "POST":
        if request.form['btn_Go_Back'] == 'Go Back':
            return redirect(url_for('main_Menu'))
    else:
        from Backend import get_Current_Balance_Information_From_Database
        from ViewBalances_Backend import table_Of_Values, table_Of_Changes_In_Values

        return render_template('ViewBalances.html', data = get_Current_Balance_Information_From_Database(), table_Of_Values = table_Of_Values(), changes_In_Values=table_Of_Changes_In_Values())



import os
if __name__ == '__main__':
    print(os.getcwd())
    import random, threading, webbrowser
    from Backend import programSetup
    programSetup()

    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    app.run(port=port, debug=False)