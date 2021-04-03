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


function accountPrimaryCheck() {
    if ((document.getElementById('Asset').checked) || (document.getElementById('Liability').checked)) {
        hideSpecificAccountDivTags()
        document.getElementById('AccountInformationDiv').style.display = 'none';
        document.getElementById('Account_Type_Term').style.display = 'grid';
    }
    else if((document.getElementById('Income').checked) || (document.getElementById('Expense').checked) ){
        document.getElementById('SpecificAccountTypeDiv').style.display = 'grid';
        document.getElementById('Account_Type_Term').style.display = 'none';
        document.getElementById("Current").checked = true;
        document.getElementById('AccountInformationDiv').style.display = 'block';

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