import os

from pathlib import Path
from dotenv import load_dotenv

import tools.treatment as treatment
import tools.analysis as analysis




def get_dataset_path():
    """
    Gets Raw Data Path from ENV VAR 'FINANCIAL_DATA_PATH'. 
    Returns: string.
    """

    dotenv_path = Path('app/.env')
    load_dotenv(dotenv_path=dotenv_path)
    try: 
        path = os.getenv('FINANCIAL_DATA_PATH')
        return path
    except Exception as e:
        print(f"Error: {e}, \n You should probably set the env var FINANCIAL_DATA_PATH")
        return None
    
def process_data(df):
    """
    Processing of the data and returns a list of Pandas DataFrames.
    """

    df = treatment.treat_data(df)
    df = treatment.convert_date(df)

    # Featuring month
    df['month'] = df['date'].dt.month

    # Calculate total expenses per payment type by month
    expenses_per_type_month = analysis.get_expenses_per_type_month(df)

    # Calculate total expenses per category by month
    expenses_per_category_month = analysis.get_expenses_per_category_month(df)

    # Calculate total expenses per subcategory by month
    expenses_per_subcategory_month = analysis.get_expenses_per_subcategory_month(df)

    return [expenses_per_type_month, expenses_per_category_month, expenses_per_subcategory_month]

def run_process_data():
    """
    Trigger for Running all the data processing pipeline. 
    Returns: a list with 3 analytical Pandas DataFrames. 
    """
    return process_data(treatment.read_data(get_dataset_path()))


# Process raw data to create analytical data
data = run_process_data()