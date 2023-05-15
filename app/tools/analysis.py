import pandas as pd

def get_expenses_per_type_month(df):
    """
    Calculates the total expenses per payment type by month and returns a pandas DataFrame.
    """
    try:
        expenses_per_type_month = df.groupby(['payment_type', 'month'])['price'].sum().reset_index()
    except KeyError:
        print("Error: Required columns not found in DataFrame.")
        return None
    else:
        return expenses_per_type_month


def get_expenses_per_category_month(df):
    """
    Calculates the total expenses per category by month and returns a pandas DataFrame.
    """
    try:
        expenses_per_category_month = df.groupby(['category', 'month'])['price'].sum().reset_index()
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
        expenses_per_subcategory_month = df.groupby(['subcategory', 'month'])['price'].sum().reset_index()
    except KeyError:
        print("Error: Required columns not found in DataFrame.")
        return None
    else:
        return expenses_per_subcategory_month