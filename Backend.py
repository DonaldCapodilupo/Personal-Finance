import datetime, os


def get_Date():
    today = str(datetime.date.today().strftime('%m/%d/%Y'))
    return today


#CRUD for "Financial Data.csv"
def create_Database_Row(account_type, account_name, account_value):
    import csv
    with open("Financial Data.csv", "a", newline="\n") as csv_file:
        csv_out = csv.writer(csv_file)

        csv_out.writerow([get_Date(), account_type,account_name, account_value])

def read_Database_Information():
    import pandas as pd

    df = pd.read_csv("Financial Data.csv", index_col=False)
    df.columns = [c.replace(' ', '_') for c in df.columns]
    return df#.to_string(index=False)

def update_Database_Information(value_to_update):
    import pandas as pd

    df = pd.read_csv("Financial Data.csv")
    df["Value"] = value_to_update
    df.to_csv("Financial Data.csv", index=False)

def delete_Database_Row(value_to_remove):
    #remove_value = ','.join(value_to_remove) +"\n"

    with open('Financial Data.csv', "r") as inp:
        data_in = inp.readlines()
    with open('Financial Data.csv', 'w') as outfile:
        for row in data_in:
            if row.split(",")[1:-1] == value_to_remove.split(",")[1:-1]:
                pass
            else:
                outfile.writelines(row)


