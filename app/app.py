import pandas as pd

import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


#Read the data
path = "data.csv"
df = pd.read_csv(path)


#Data treatment
analitycal = df[['data','tipo_pagamento', 'valor','categoria','grupo_categoria']] # <-- adapt to your data
analitycal['valor'] = analitycal['valor'].str.replace(',','.')
analitycal = analitycal.astype({'valor':'float'})


# Convert the date on ["data"] to "YYYY-MM-DD" format using pandas to_datetime() function
for i, date in enumerate(analitycal['data']):
    #dealing with two year pattern data entry ex: "2023" and "23"
    if len(date) == 8:
        analitycal.loc[i, 'data'] = pd.to_datetime(date, format='%d/%m/%y').strftime('%Y-%m-%d')
    else:
        analitycal.loc[i, 'data'] = pd.to_datetime(date, format='%d/%m/%Y').strftime('%Y-%m-%d')

# Casting from string to datetime
analitycal["data"] = pd.to_datetime(analitycal['data'], format='%Y-%m-%d')

# Featuring month
analitycal['mes'] = analitycal['data'].dt.month

# Calculate total expenses per payment type by month
expenses_per_type_month = analitycal.groupby(['tipo_pagamento', 'mes'])['valor'].sum().reset_index()

# Calculate total expenses per payment type
expenses_per_type = analitycal.groupby(['tipo_pagamento'])['valor'].sum().reset_index()

# Calculate total expenses per category by month
expenses_per_category_month = analitycal.groupby(['categoria', 'mes'])['valor'].sum().reset_index()

# Calculate total expenses per subcategory by month
expenses_per_subcategory_month = analitycal.groupby(['grupo_categoria', 'mes'])['valor'].sum().reset_index()


# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the dashboard
app.layout = dbc.Container(
    [
        html.H1('Análise Financeira'),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=px.line(expenses_per_type_month, x='mes', y='valor', color='tipo_pagamento', 
                                       labels={'mes': 'Mês', 'valor': 'Valor', 'tipo_pagamento': 'Tipo de Pagamento'},
                                       title='Despesas por tipo de pagamento por mês')
                    )
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=px.bar(expenses_per_category_month, x='mes', y='valor', color='categoria', 
                                      labels={'mes': 'Mês', 'valor': 'Valor', 'categoria': 'Categoria'},
                                      title='Despesas por categoria por mês')
                    )
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=px.bar(expenses_per_subcategory_month, x='mes', y='valor', color='grupo_categoria', 
                                      labels={'mes': 'Mês', 'valor': 'Valor', 'grupo_categoria': 'Subcategoria'},title='Despesas por subcategoria por mês')))
    ]
    
)
    ], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)