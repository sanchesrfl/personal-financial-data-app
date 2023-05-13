import data

def process_data(df):
    """
    Processing of the data and returns a list of Pandas DataFrames.
    """

    df = data.treat_data(df)
    df = data.convert_date(df)

    # Featuring month
    df['month'] = df['date'].dt.month

    # Calculate total expenses per payment type by month
    expenses_per_type_month = data.get_expenses_per_type_month(df)

    # Calculate total expenses per category by month
    expenses_per_category_month = data.get_expenses_per_category_month(df)

    # Calculate total expenses per subcategory by month
    expenses_per_subcategory_month = data.get_expenses_per_subcategory_month(df)

    return [expenses_per_type_month, expenses_per_category_month, expenses_per_subcategory_month]


# Process raw data to create analytical data
path = "data.csv"
data = process_data(data.read_data(path))