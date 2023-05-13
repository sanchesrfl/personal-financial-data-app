
import dash

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.express as px

import data_processing.processing as p

def create_layout(expenses_per_type_month,expenses_per_category_month,expenses_per_subcategory_month):
    """
    Creates the layout for the Dash app.

    Returns:
    - A Dash Container containing the layout.
    """
    layout = dbc.Container(
        [
        html.H1('Análise Financeira'),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=px.line(expenses_per_type_month, x='month', y='price', color='payment_type', 
                                       labels={'month': 'Month', 'price': 'Price', 'payment_type': 'Payment Type'},
                                       title='Expenses per type and month')
                    )
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=px.bar(expenses_per_category_month, x='month', y='price', color='category', 
                                      labels={'month': 'Month', 'price': 'Price', 'category': 'Category'},
                                      title='Expenses per category and month')
                    )
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=px.bar(expenses_per_subcategory_month, x='month', y='price', color='subcategory', 
                                      labels={'month': 'Month', 'price': 'Price', 'subcategory': 'Subcategory'},
                                      title='Expenses per subcategory and month')))
    ]
    
)
    ], fluid=True)

    return layout


# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Inject layout to Dash App
app.layout = create_layout(*p.data)
