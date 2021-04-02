from flask import Flask, render_template, request,url_for,redirect

app = Flask(__name__)





@app.route('/', methods=["POST","GET"])
def main_Menu():
    if request.method == "POST":
        if request.form['btn'] == 'Update Account Balances':
            return redirect(url_for('update_Accounts'))
        if request.form['btn'] == 'Add an Account':
            return redirect(url_for('add_Account'))
        if request.form['btn'] == 'Remove an Account':
            return redirect(url_for('remove_Account'))
        if request.form['btn'] == 'View Account Balances':
            return redirect(url_for('view_Balances'))
    else:
        return render_template('main.html')


@app.route('/UpdateAccountBalances', methods=["POST","GET"])
def update_Accounts():
    if request.method == "POST":
        if request.form['btn_Go_Back'] == 'Go Back':
            return redirect(url_for('main_Menu'))
    else:
        return render_template('UpdateAccounts.html')


@app.route('/AddAnAccount', methods=["POST","GET"])
def add_Account():
    skip_Term_Div = ('Income','Expense')
    #if request.method == "POST":
    #    if request.form['submit'] == 'Go Back':
    #        return redirect(url_for('main_Menu'))

    #else:
    return render_template('AddAccount.html')

@app.route('/RemoveAnAccount', methods=["POST","GET"])
def remove_Account():
    if request.method == "POST":
        if request.form['btn_Go_Back'] == 'Go Back':
            return redirect(url_for('main_Menu'))
    else:
        return render_template('RemoveAccounts.html')

@app.route('/ViewAccountBalances', methods=["POST","GET"])
def view_Balances():
    if request.method == "POST":
        if request.form['btn_Go_Back'] == 'Go Back':
            return redirect(url_for('main_Menu'))
    else:
        return render_template('ViewBalances.html')




if __name__ == '__main__':
    import random, threading, webbrowser

    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    app.run(port=port, debug=False)