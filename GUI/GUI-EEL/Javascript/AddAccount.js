function goBack() {
    window.open("main.html","_self");
}

function getAccountType() {
    const asset = Boolean(document.getElementById("Asset").checked);
    const liability = Boolean(document.getElementById("Liability").checked);
    const income = Boolean(document.getElementById("Income").checked);
    const expense = Boolean(document.getElementById("Expense").checked);
    const current = Boolean(document.getElementById("Current").checked);
    const noncurrent = Boolean(document.getElementById("NonCurrent").checked);
    const currentAsset = document.getElementById("FinalCurrentAsset");
    const nonCurrentAsset = document.getElementById("FinalNonCurrentAsset");
    const currentLiability = document.getElementById("FinalCurrentLiability");
    const nonCurrentLiability = document.getElementById("FinalNonCurrentLiability");

    const specificAccountType = document.getElementById("SpecificAccountTypeDiv");



    if (asset && current){
        currentAsset.style.display = "block";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "none";
        specificAccountType.style.display = "block";
    }

    else if(asset && noncurrent){
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "block";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "none";
        specificAccountType.style.display = "block";
    }
    else if(liability && current){
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "block";
        nonCurrentLiability.style.display = "none";
        specificAccountType.style.display = "block";
    }
    else if(liability && noncurrent){
        currentAsset.style.display = "none";
        nonCurrentAsset.style.display = "none";
        currentLiability.style.display = "none";
        nonCurrentLiability.style.display = "block";
        specificAccountType.style.display = "block";
    }

    else{
        let newText = document.getElementById("AccountTermID");
        let warningError = document.createTextNode("Please select one of each section.");

        newText.remove()
        newText.appendChild(warningError);
    }

}

function accountPrimaryCheck() {
    if ((document.getElementById('Asset').checked) || (document.getElementById('Liability').checked)) {
        document.getElementById('AccountTermID').style.display = 'grid';
        document.getElementById('SpecificAccountTypeDiv').style.display = 'none';
    }
    else if((document.getElementById('Income').checked) || (document.getElementById('Expense').checked) ){
        document.getElementById('SpecificAccountTypeDiv').style.display = 'grid';
        document.getElementById('AccountTermID').style.display = 'none';

    }


        else {
        document.getElementById('AccountTermID').style.display = 'none';

    }
}



function check() {
    document.getElementById("red").checked = true;
}

function uncheck() {
    document.getElementById("red").checked = false;
}