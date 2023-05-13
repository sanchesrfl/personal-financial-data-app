import dash
import dash_bootstrap_components as dbc

import processing as p
import layout

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Inject layout to Dash App
app.layout = layout.create_layout(*p.data)

# Run Web App
if __name__ == '__main__':
    app.run_server(debug=True)