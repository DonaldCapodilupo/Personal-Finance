document.getElementById("Results Card").style.visibility = "hidden";

function prep_Account() {
    document.getElementById("Results Card").style.visibility = "visible";
    const saved_items = [];



    let new_account_name = document.getElementById('New Account Name').value;
    let new_account_type = document.getElementById('New Account Type').value;
    let new_account_balance = document.getElementById('New Account Balance').value;

    let results_area = document.getElementById("Data Area");
    console.log(results_area.value);

    if (results_area.value.length === 0){
        results_area.value += new_account_type + "," + new_account_name + "," + new_account_balance;
    }else{
        results_area.value += "\n" + new_account_type + "," + new_account_name + "," + new_account_balance;
    }



}
