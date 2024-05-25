import pandas as pd
from datetime import datetime
import os

# Location of the data directory
csv_location = f'{os.getcwd()}\\data\\transactions.csv'

# Columns of the CSV file
df_columns = ['Last Modified', 'Transaction Date', 'Transaction Type', 'Description', 'Vendor', 'Price', 'Business Money', 'Personal Money', 'Paid']

# Check to create the directory if it doesn’t exist, ensuring the file path is always valid
if not os.path.exists(os.path.dirname(csv_location)):
    os.makedirs(os.path.dirname(csv_location))

# Function to initialize dataframe with data from csv. If no csv, creates new one and initializes dataframe
def initialize_dataframe():
    # Try to read CSV data into dataframe; creates a new file if not found and initializes the dataframe
    try:
        df = pd.read_csv(csv_location)
    except FileNotFoundError:
        print('Data file not found, creating new CSV file')
        df = pd.DataFrame(columns = df_columns)
        df.to_csv(csv_location, index=False)
    return df

# Function to add a purchase to the transactions CSV
def add_transaction(transaction_date: str, 
                    description: str, 
                    transaction_type: str,
                    vendor: str, 
                    price: float, 
                    business_money: float, 
                    personal_money: float, 
                    paid: bool):
    '''
    Function to add a purchase to the transactions dataframe
    -> Returns: Dataframe containing the added record
    
    Params:
    - Transaction type: (Purchase, sale, payment)
    - Transaction date: (Date of transaction "d/m/y")
    - Description: (Name of what purchased, if sale then PC ID, if payment then description of what was purchased)
    - Vendor: (Facebook Marketplace, EBAY, Best Buy, etc.)
    - Price: (100, 500, 350, etc.)
    - Business money: (How much spent or earned)
    - Personal money: (How much spent or earned)
    - Paid (True, False)
    '''
    # Creates a new dateframe with existing date if there was any
    df = initialize_dataframe()
    
    # Appends purchase data to dictionary
    new_record = {
        'Last Modified': datetime.now().strftime("%d/%m/%Y"), # Gets the current date when the command is executed
        'Transaction Date': transaction_date,
        'Transaction Type': transaction_type,
        'Description': description,
        'Vendor': vendor,
        'Price': price,
        'Business Money': business_money,
        'Personal Money': personal_money,
        'Paid': paid,
    }

    # Appends the data from the dictionary to the dataframe and returns
    df = df._append(new_record, ignore_index = True)
    return df
    
def add_sale(transaction_date : str, computer : str, price : str):
    '''
    Function to add a sale to the transactions CSV
    Returns: Dataframe containing the added data
    '''
    df = initialize_dataframe()

    # Appends sale data to dictionary
    new_sale = {
        'Last Modified': datetime.now().strftime("%d/%m/%Y"), # Gets the current date when the command is executed
        'Transaction Date': transaction_date,
        'Transaction Type': 'Purchase',
        'Description': computer,
        'Vendor': 'N/A',
        'Price': price,
        'Business Money': price,
        'Personal Money': 0.00,
        'Paid': True,
    }

    df = df._append(new_sale, ignore_index = True)
    df.to_csv(csv_location, index = False)