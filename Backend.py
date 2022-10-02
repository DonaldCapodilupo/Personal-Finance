import datetime, os

#Basic Functions
def programSetup():
    if "Financial Data.csv" not in os.listdir():
        with open("Financial Data.csv", "w", newline="") as csv_file:
            csv_file.write("Date,Account Type,Account Name,Value\n" )

def get_Date():
    today = str(datetime.date.today().strftime('%m/%d/%Y'))
    return today

def raw_Num_To_Currency(raw_Number: float):
    return "${:,.2f}".format(raw_Number)

def raw_Num_To_Percentage(raw_Number: float):
    return "{:,.2f}%".format(raw_Number)


#CRUD for "Financial Data.csv"
def create_Database_Row(tuple_of_values_to_add):
    import csv
    with open("Financial Data.csv", "a", newline="\n") as csv_file:
        csv_out = csv.writer(csv_file)
        csv_out.writerow(tuple_of_values_to_add)

def read_Database_Information():
    import pandas as pd

    df = pd.read_csv("Financial Data.csv", index_col=False)
    df.columns = [c.replace(' ', '_') for c in df.columns]
    return df#.to_string(index=False)

def update_Database_Information(value_to_update):
    with open('Financial Data.csv', "r") as inp:
        data_in = inp.readlines()
    with open('Financial Data.csv', 'w') as outfile:
        for row in data_in:
            row_to_tuple = tuple(row.split(","))
            if row_to_tuple[1:-1] == value_to_update[1:-1]:
                update_value = (get_Date(),) + row_to_tuple[1:-1] + (value_to_update[-1],)
                print(update_value)
                outfile.writelines(','.join(update_value) +"\n")
            else:
                outfile.writelines(row)

def delete_Database_Row(value_to_remove):
    #remove_value = ','.join(value_to_remove) +"\n"

    with open('Financial Data.csv', "r") as inp:
        data_in = inp.readlines()
    with open('Financial Data.csv', 'w') as outfile:
        for row in data_in:
            print(type(row.split(",")))
            print("****************")
            print(type(value_to_remove.split(",")))
            if row.split(",")[1:-1] == value_to_remove.split(",")[1:-1]:
                pass
            else:
                outfile.writelines(row)






def organize_Database(dataframe):
    account_Type_Nums = {
        "Current Asset": 0,
        "NonCurrent Asset": 1,
        "Current Liability": 2,
        "NonCurrent Liability": 3,
    }



    dataframe["Account Type Number"] = [account_Type_Nums[account] for account in
                                                dataframe["Account_Type"].values]

    organized_Dataframe = dataframe.sort_values(by=["Account Type Number", "Date"])
    organized_Dataframe = organized_Dataframe.drop(["Account Type Number"], axis=1)

    return organized_Dataframe

def prior_Report_Dates():
    today = str(datetime.date.today())
    end_Of_Year = today[0:2] + str(int(today[2:4]) - 1) + '-12-31'

    current_Balances = read_Database("Account_Balances.db", "Accounts")
    for row in current_Balances.values:
        date_Current_Balances = row[1]
        break

    ref = datetime.date.today()
    if ref.month < 4:
        return end_Of_Year, str(datetime.date(ref.year - 1, 12, 31)), today
    elif ref.month < 7:
        return end_Of_Year, str(datetime.date(ref.year, 3, 31)), today
    elif ref.month < 10:
        return end_Of_Year, str(datetime.date(ref.year, 6, 30)), today
    return end_Of_Year, str(datetime.date(ref.year, 9, 30)), today

def difference_Between_Percentage_Calculator(previous_Value: float, current_Value: float):
    import decimal
    try:
        return "{:,.2f}%".format(((current_Value - previous_Value) / previous_Value) * 100)
    except (decimal.DivisionByZero, decimal.InvalidOperation):
        return "0.00%"




def percentage_Or_Currency_To_Float(input_String: str):
    from re import sub
    from decimal import Decimal

    return Decimal(sub(r'[^\d.-]', '', input_String))


def create_Account_Balances_HTML_Table():
    import pandas as pd

    balances = {
       "EOY": {"Current Asset": 0.00,
               "NonCurrent Asset": 0.00,
               "Total Assets": 0.00,
               "Current Liability": 0.00,
               "NonCurrent Liability": 0.00,
               "Total Liabilities": 0.00,
               "Equity": 0.00},
       "EOQ": {"Current Asset": 0.00,
                   "NonCurrent Asset": 0.00,
                   "Total Assets": 0.00,
                   "Current Liability": 0.00,
                   "NonCurrent Liability": 0.00,
                   "Total Liabilities":0.00,
                   "Equity": 0.00},
       "Current": {"Current Asset": 0.00,
                   "NonCurrent Asset": 0.00,
                   "Total Assets": 0.00,
                   "Current Liability": 0.00,
                   "NonCurrent Liability": 0.00,
                   "Total Liabilities": 0.00,
                   "Equity": 0.00},
    }

    for row in read_Database("Backup_Balances.db", "Accounts").values:
        if row[1] == prior_Report_Dates()[0]:
            balances["EOY"][row[2]] += float(row[4])
        elif row[1] == prior_Report_Dates()[1]:
            balances["EOQ"][row[2]] += float(row[4])

    for row in read_Database("Account_Balances.db", "Accounts").values:
        balances["Current"][row[2]] += float(row[4])

    for key in balances:
        balances[key]["Total Assets"] = balances[key]["Current Asset"] + balances[key]["NonCurrent Asset"]
        balances[key]["Total Liabilities"] = balances[key]["Current Liability"] + balances[key]["NonCurrent Liability"]
        balances[key]["Equity"] = balances[key]["Total Assets"] - balances[key]["Total Liabilities"]

    for key in balances:
        for nested_Dict in balances[key]:
            balances[key][nested_Dict] = raw_Num_To_Currency(balances[key][nested_Dict])


    balances_Html = pd.DataFrame.from_dict(balances)
    balances_Html.to_html("templates/Account_Balances_Table.html", classes="table")

    return balances


def get_Account_Percentages():
    import pandas as pd

    balances = create_Account_Balances_HTML_Table()

    percentages = {"YTD $ Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""},
                   "YTD % Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""},
                   "QTD $ Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""},
                   "QTD % Change": {"Current Asset": "",
                                    "NonCurrent Asset": "",
                                    "Total Assets": "",
                                    "Current Liability": "",
                                    "NonCurrent Liability": "",
                                    "Total Liabilities": "",
                                    "Equity": ""}
                   }


    for table_Column in percentages:
        if "YTD %" in table_Column:
            for table_Row in percentages[table_Column]:

                percentages[table_Column][table_Row] = difference_Between_Percentage_Calculator(
                    percentage_Or_Currency_To_Float(balances["EOY"][table_Row]),
                    percentage_Or_Currency_To_Float(balances["Current"][table_Row])
                )
        elif "YTD $" in table_Column:
            for table_Row in percentages[table_Column]:
                percentages[table_Column][table_Row] = raw_Num_To_Currency (
                            percentage_Or_Currency_To_Float(balances["Current"][table_Row]) -
                            percentage_Or_Currency_To_Float(balances["EOY"][table_Row])
                            )
        elif "QTD %" in table_Column:
            for table_Row in percentages[table_Column]:

                percentages[table_Column][table_Row] = difference_Between_Percentage_Calculator(
                    percentage_Or_Currency_To_Float(balances["EOQ"][table_Row]),
                    percentage_Or_Currency_To_Float(balances["Current"][table_Row])
                )
        elif "QTD $" in table_Column:
            for table_Row in percentages[table_Column]:
                percentages[table_Column][table_Row] = raw_Num_To_Currency(
                    percentage_Or_Currency_To_Float(balances["Current"][table_Row]) -
                    percentage_Or_Currency_To_Float(balances["EOQ"][table_Row])
                )

    percentages_HTML = pd.DataFrame.from_dict(percentages)
    percentages_HTML.to_html("templates/Account_Percentages_Table.html", classes="table", index=False)

    return percentages


def create_Balance_Sheet_HTML():
    current_Balances_Database = read_Database("Account_Balances.db", "Accounts")

    # Rearange to current assets, noncurrent assets, total assets, etc.
    account_Type_Nums = {
        "Current Asset": 1,
        "NonCurrent Asset": 2,
        "Current Liability": 3,
        "NonCurrent Liability": 4,
    }
    current_Balances_Database["Account Type Number"] = [account_Type_Nums[account] for account in
                                                        current_Balances_Database["Account_Type"].values]
    current_Balances_Database = current_Balances_Database.sort_values(by=["Account Type Number"])

    # Add the "currenct balance in $" column
    current_Balances_Database["Current Value"] = [raw_Num_To_Currency(float(dollar_Amount)) for dollar_Amount in
                                                  current_Balances_Database["Value"].values]

    # drop unneeded columns
    balance_Sheet = current_Balances_Database.drop(['Account_Type', 'Value'], axis=1)

    # save file
    balance_Sheet.to_html("templates/Balance_Sheet.html", index=False, classes="table")

def get_Monthly_Account_Balances_Dict():
    import pandas as pd

    prior_Balances = read_Database("Backup_Balances.db", "Accounts")

    return_Dict = {}


    prior_Months = pd.date_range(prior_Report_Dates()[0], str(datetime.date.today()),
                  freq='MS').strftime("%Y-%b").tolist()


    #for row in



    for row in prior_Months:
        return_Dict[row[5:]] = ""

    daterange = pd.date_range(prior_Report_Dates()[0], str(datetime.date.today()), freq='1M').tolist()
    daterange = [d.strftime('%y-%b') for d in daterange]
    print(daterange)


    print(return_Dict)


