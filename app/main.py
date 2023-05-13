import dash
import dash_bootstrap_components as dbc

import data
import layout


# Read the data
path = "data.csv"
df = data.read_data(path)

# Treats the data
df = data.treat_data(df)

# Convert the date column to "YYYY-MM-DD" format
df = data.convert_date(df)

# Featuring month
df['mes'] = df['data'].dt.month

# Calculate total expenses per payment type by month
expenses_per_type_month = data.get_expenses_per_type_month(df)

# Calculate total expenses per category by month
expenses_per_category_month = data.get_expenses_per_category_month(df)

# Calculate total expenses per subcategory by month
expenses_per_subcategory_month = data.get_expenses_per_subcategory_month(df)

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Inject layout to Dash App
app.layout = layout.create_layout(expenses_per_type_month,expenses_per_category_month,expenses_per_subcategory_month)

# Run Web App
if __name__ == '__main__':
    app.run_server(debug=True)