import pandas as pd
def read_data(path):
    """
    Reads data from a csv file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None
    else:
        return df
    
def treat_data(df):
    """
    Treat some inconvinients from data entry and returns a clean pandas DataFrame.
    """

    try:
        df = df[['data','tipo_pagamento', 'valor','categoria','sub_categoria']] #<-- adapts for your data.
        df['valor'] = df['valor'].str.replace(',','.')
        df = df.astype({'valor':'float'})
        return df
    except ValueError:
        print(f"Error: {ValueError}")
        return None
        


def convert_date(df, date_col='data'):
    """
    Converts the date column in the given DataFrame to the "YYYY-MM-DD" format.
    """
    try:
        #dealing with two year pattern data entry ex: "2023" and "23"
        df[date_col] = df[date_col].str.replace(',','.')
        for i, date in enumerate(df[date_col]):
            if len(date) == 8:
                df.loc[i, date_col] = pd.to_datetime(date, format='%d/%m/%y').strftime('%Y-%m-%d')
            else:
                df.loc[i, date_col] = pd.to_datetime(date, format='%d/%m/%Y').strftime('%Y-%m-%d')
        df[date_col] = pd.to_datetime(df[date_col], format='%Y-%m-%d')
    except KeyError:
        print(f"Error: Date column '{date_col}' not found in DataFrame.")
        return None
    except ValueError:
        print(f"Error: Invalid date format in column '{date_col}'.")
        return None
    else:
        return df


def get_expenses_per_type_month(df):
    """
    Calculates the total expenses per payment type by month and returns a pandas DataFrame.
    """
    try:
        expenses_per_type_month = df.groupby(['tipo_pagamento', 'mes'])['valor'].sum().reset_index()
    except KeyError:
        print("Error: Required columns not found in DataFrame.")
        return None
    else:
        return expenses_per_type_month


def get_expenses_per_type(df):
    """
    Calculates the total expenses per payment type and returns a pandas DataFrame.
    """
    try:
        expenses_per_type = df.groupby(['tipo_pagamento'])['valor'].sum().reset_index()
    except KeyError:
        print("Error: Required columns not found in DataFrame.")
        return None
    else:
        return expenses_per_type


def get_expenses_per_category_month(df):
    """
    Calculates the total expenses per category by month and returns a pandas DataFrame.
    """
    try:
        expenses_per_category_month = df.groupby(['categoria', 'mes'])['valor'].sum().reset_index()
    except KeyError:
        print("Error: Required columns not found in DataFrame.")
        return None
    else:
        return expenses_per_category_month


def get_expenses_per_subcategory_month(df):
    """
    Calculates the total expenses per subcategory by month and returns a pandas DataFrame.
    """
    try:
        expenses_per_subcategory_month = df.groupby(['sub_categoria', 'mes'])['valor'].sum().reset_index()
    except KeyError:
        print("Error: Required columns not found in DataFrame.")
        return None
    else:
        return expenses_per_subcategory_month