import dash
from dash import html

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Hello, Dash!", style={'textAlign': 'center'})
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)