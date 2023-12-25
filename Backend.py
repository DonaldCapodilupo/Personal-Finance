import datetime, os, json


def get_Date():
    today = str(datetime.date.today().strftime('%m/%d/%Y'))
    return today


def setup_Program():
    file_name = "static/Account History/" + get_Date().replace("/", "") + ".json"
    if "Account History" not in os.listdir("static"):
        os.mkdir("static/Account History")

        # Opening JSON file
        with open('template.json', 'r') as openfile:
            # Reading from json file
            template_json = json.load(openfile)

        with open(file_name, "w") as out_file:
            json.dump(template_json, out_file)

    if get_Date().replace("/", "")+".json" not in os.listdir("static/Account History"):

        prior_completed_balance_sheet ="static/Account History/"+ os.listdir("static/Account History")[-1]
        # Opening JSON file
        with open(prior_completed_balance_sheet, 'r') as openfile:
            # Reading from json file
            template_json = json.load(openfile)

        with open(file_name, "w") as out_file:
            json.dump(template_json, out_file)

        # CRUD for "Financial Data.csv"


def create_Database_Row(account_type, account_name, account_value):
    file_name = "static/Account History/" + get_Date().replace("/", "") + ".json"


    with open(file_name,"r") as infile:
        current_balance_sheet_accounts = json.load(infile)

    current_balance_sheet_accounts[account_type][account_name] = account_value

    json_obj = json.dumps(current_balance_sheet_accounts)

    with open(file_name, "w") as json_file:
        json_file.write(json_obj)




def read_Database_Information():
    file_name = "static/Account History/" + get_Date().replace("/", "") + ".json"
    with open(file_name, "r") as infile:
        current_balance_sheet_accounts = json.load(infile)
    return current_balance_sheet_accounts


def update_Database_Information(value_to_update):
    file_name = "static/Account History/" + get_Date().replace("/", "") + ".json"
    with open(file_name, "r") as infile:
        current_balance_sheet_accounts = json.load(infile)

    new_dict = {
        "Current Assets": {},
        "Noncurrent Assets": {},
        "Current Liabilities": {},
        "Noncurrent Liabilities": {}
    }

    for account in current_balance_sheet_accounts:
        for account_name, account_value in current_balance_sheet_accounts[account].items():
            if account_name in value_to_update.keys():
                new_dict[account][account_name] = value_to_update[account_name]



    with open(file_name, "w") as out_file:
            json.dump(new_dict, out_file)

def delete_Database_Row(values_to_remove):
    # remove_value = ','.join(value_to_remove) +"\n"
    file_name = "static/Account History/" + get_Date().replace("/", "") + ".json"
    with open(file_name, "r") as infile:
        current_balance_sheet_accounts = json.load(infile)
        print(type(current_balance_sheet_accounts))

    new_dict = {
        "Current Assets":{},
        "Noncurrent Assets": {},
        "Current Liabilities": {},
        "Noncurrent Liabilities": {}
    }

    for account_type in current_balance_sheet_accounts.keys():
            for account_name, account_balance in current_balance_sheet_accounts[account_type].items():
                if account_name not in values_to_remove:
                    new_dict[account_type][account_name] = account_balance

    with open(file_name, "w") as out_file:
        json.dump(new_dict, out_file)