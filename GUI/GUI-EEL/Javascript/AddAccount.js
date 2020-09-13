
//Function to get values. Eel (Python) will be able to access this function.

function getRadioVal(generic, specific, term, description, value) {
    let genericVal, termVal, specificVal;
    // get list of radio buttons with specified name
    const radioGeneric = document.getElementsByName(generic);
    const radioSpecific = document.getElementsByName(specific);
    const radioTerm = document.getElementsByName(term);
    const userDescription = document.getElementById(description).value;
    const userValue = document.getElementById(value).value;


    // loop through list of radio buttons
    for (let i=0, len=radioGeneric.length; i<len; i++) {
        if ( radioGeneric[i].checked ) { // radio checked?
            genericVal = radioGeneric[i].value; // if so, hold its value in val
            break; // and break out of for loop
        }
    }

    for (let i=0, len=radioSpecific.length; i<len; i++) {
        if ( radioSpecific[i].checked ) { // radio checked?
            termVal = radioSpecific[i].value; // if so, hold its value in val
            break; // and break out of for loop
        }
    }

    for (let i=0, len=radioTerm.length; i<len; i++) {
        if ( radioTerm[i].checked ) { // radio checked?
            specificVal = radioTerm[i].value; // if so, hold its value in val
            break; // and break out of for loop
        }
    }



    console.log(genericVal,termVal,specificVal, userDescription, userValue);
    eel.printRadioButtonValues(genericVal,termVal, specificVal, userDescription, userValue);
    eel.addAccountToDatabase(genericVal,termVal, specificVal, userDescription, userValue);
}


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

//These functions reveals div tags based on a button click relative to which radio button is clicked.
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
