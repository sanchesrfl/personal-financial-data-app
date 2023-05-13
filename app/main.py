import flask_viz_app.dashboard as dashboard


# Run WebDash App
if __name__ == '__main__':
    dashboard.app.run_server(debug=True)
