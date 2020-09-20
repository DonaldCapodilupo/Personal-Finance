//Buttons
function goBack() {
    window.open("main.html","_self");
}


//These functions reveal div tags based on a button click relative to which radio button is clicked.
function getAccountType() {
    const asset = Boolean(document.getElementById("Asset").checked);
    const liability = Boolean(document.getElementById("Liability").checked);
    const income = Boolean(document.getElementById("Income").checked);
    const expense = Boolean(document.getElementById("Expense").checked);
    const current = Boolean(document.getElementById("Current").checked);
    const nonCurrent = Boolean(document.getElementById("NonCurrent").checked);
    const currentAsset = document.getElementById("FinalCurrentAsset");
    const nonCurrentAsset = document.getElementById("FinalNonCurrentAsset");
    const currentLiability = document.getElementById("FinalCurrentLiability");
    const nonCurrentLiability = document.getElementById("FinalNonCurrentLiability");
    const incomeSpecific = document.getElementById("IncomeSpecific");
    const expensesSpecific = document.getElementById("ExpensesSpecific");



    const specificAccountType = document.getElementById("SpecificAccountTypeDiv");

    document.getElementById('AccountInformationDiv').style.display = 'block';


    if (asset && current) {
        currentAsset.style.display = "block";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "none";
        specificAccountType.style.display = "block";
    } else if (asset && nonCurrent) {
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "block";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "none";
        specificAccountType.style.display = "block";
    } else if (liability && current) {
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "block";
        nonCurrentLiability.style.display = "none";
        specificAccountType.style.display = "block";
    } else if (liability && nonCurrent) {
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "block";
        specificAccountType.style.display = "block";
    } else if (income && current) {
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "none";
        incomeSpecific.style.display = "block"
        expensesSpecific.style.display = "none"
        specificAccountType.style.display = "block";
    } else if (expense && current) {
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "none";
        incomeSpecific.style.display = "none"
        expensesSpecific.style.display = "block"
        specificAccountType.style.display = "block";
    }
}


function hideSpecificAccountDivTags(){
    const currentAsset = document.getElementById("FinalCurrentAsset");
    const nonCurrentAsset = document.getElementById("FinalNonCurrentAsset");
    const currentLiability = document.getElementById("FinalCurrentLiability");
    const nonCurrentLiability = document.getElementById("FinalNonCurrentLiability");
    const incomeSpecific = document.getElementById("IncomeSpecific");
    const expensesSpecific = document.getElementById("ExpensesSpecific");

    let hideDivsArray = [currentAsset, nonCurrentAsset, currentLiability, nonCurrentLiability, incomeSpecific,
        expensesSpecific]

    for (let eachItemInArray = 0, len = hideDivsArray.length; eachItemInArray < len; eachItemInArray++) {
        hideDivsArray[eachItemInArray].style.display = "none"
    }
}


//Determine if the user needs to determine if the Asset/Liability is long term or not.
//If the User selected Income/Expenses, then we automatically determine the item is current and not long term.
function accountPrimaryCheck() {
    if ((document.getElementById('Asset').checked) || (document.getElementById('Liability').checked)) {
        hideSpecificAccountDivTags()
        document.getElementById('AccountInformationDiv').style.display = 'none';
        document.getElementById('AccountTermID').style.display = 'grid';
    }
    else if((document.getElementById('Income').checked) || (document.getElementById('Expense').checked) ){
        document.getElementById('SpecificAccountTypeDiv').style.display = 'grid';
        document.getElementById('AccountTermID').style.display = 'none';
        document.getElementById("Current").checked = true;

        if ((document.getElementById('Income').checked)){
            hideSpecificAccountDivTags()
            const incomeSpecificDiv = document.getElementById("IncomeSpecific");
            const expensesSpecificDiv = document.getElementById("ExpensesSpecific");
            incomeSpecificDiv.style.display = "grid";
            expensesSpecificDiv.style.display = "none";
        }
        else if ((document.getElementById('Expense').checked)){
            hideSpecificAccountDivTags()
            const incomeSpecificDiv = document.getElementById("IncomeSpecific");
            const expensesSpecificDiv = document.getElementById("ExpensesSpecific");
            incomeSpecificDiv.style.display = "none";
            expensesSpecificDiv.style.display = "grid";
        }
    }
}

function getPageValues(){
    const genericAccountType = document.getElementsByName('PrimaryAccountType');
    const accountTerm = document.getElementsByName('AccountTerm');
    const specificAccountType = document.getElementsByName('Final_Account_Type');
    const userDescription = document.getElementById('accountNameBox').value;
    const userValue = document.getElementById('accountValueBox').value;

    let documentInformationArray = [genericAccountType,accountTerm, specificAccountType]

    let finalGenericAccountType;
    let finalAccountTerm;
    let finalSpecificAccountType;

    console.log(genericAccountType)


    for (let i = 0, len = documentInformationArray.length; i < len; i++) {
        for (let x = 0, xlen = documentInformationArray[i].length; x < xlen; x++) {
            console.log(documentInformationArray[i])
            console.log(documentInformationArray[i][x])
            if (documentInformationArray[i][x].checked) { // radio checked?
                documentInformationArray[i] = documentInformationArray[i][x].value; // if so, hold its value in val
                console.log(documentInformationArray)
                break; // and break out of for loop
            }
        }
    }



    console.log(
        "Generic account type: " + documentInformationArray[0],
        +"\nAccount term: " + documentInformationArray[1]
        + "\nSpecific account type: " + documentInformationArray[2]
        + "\nAccount description: " + userDescription
        + "\nAccount value: " + userValue);

    //Print output to Python
    eel.printRadioButtonValues(
        documentInformationArray[0],
        documentInformationArray[1],
        documentInformationArray[2],
        userDescription,
        userValue);

    //Add all of the current values of the object into the database.
    eel.addAccountToDatabase(
        documentInformationArray[0],
        documentInformationArray[1],
        documentInformationArray[2],
        userDescription,
        userValue);


}

