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
        df.to_csv(csv_location)
    return df

# Function to add a purchase to the transactions CSV
def add_purchase(transaction_date, description, vendor, price : float, business_spent : float, personal_spent : float, paid : bool):  
    '''
    Function to add a purchase to the transactions CSV
    Returns: Dataframe containing the added data
    '''
    df = initialize_dataframe()
    
    # Appends purchase data to dictionary
    new_purchase = {
        'Last Modified': datetime.now().strftime("%d/%m/%Y"), # Gets the current date when the command is executed
        'Transaction Date': transaction_date,
        'Transaction Type': 'Purchase',
        'Description': description,
        'Vendor': vendor,
        'Price': price,
        'Business Money': business_spent,
        'Personal Money': personal_spent,
        'Paid': paid,
    }

    # Appends the data from the dictionary to the dataframe and adds the data to the csv
    df = df._append(new_purchase, ignore_index = True)
    df.to_csv(csv_location, index = False)

    return df
    
def add_sale(transaction_date, computer, price):
    '''
    Function to add a sale to the transactions CSV
    Returns: Dataframe containing the added data
    '''
    df = initialize_dataframe()

    # Appends sale data to dictionary
    new_purchase = {
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