import plotly.express as px

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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
                        figure=px.bar(expenses_per_subcategory_month, x='mes', y='valor', color='sub_categoria', 
                                      labels={'mes': 'Mês', 'valor': 'Valor', 'sub_categoria': 'Subcategoria'},title='Despesas por subcategoria por mês')))
    ]
    
)
    ], fluid=True)

    return layout