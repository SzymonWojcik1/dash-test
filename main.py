import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Charger les données
df = pd.DataFrame({
    'Catégorie': ['A', 'B', 'C', 'D', 'E'],
    'Valeur': [10, 20, 15, 25, 30]
})

# Initialiser l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Dashboard Interactif avec Dash"),

    dcc.Dropdown(
        id='dropdown_categorie',
        options=[{'label': cat, 'value': cat} for cat in df['Catégorie']],
        value='A',
        clearable=False
    ),

    dcc.Graph(id='graphique')
])

# Callback pour mettre à jour le graphique
@app.callback(
    Output('graphique', 'figure'),
    Input('dropdown_categorie', 'value')
)

def update_graph(selected_category):
    df_filtered = df[df['Catégorie'] == selected_category]
    fig = px.bar(df_filtered, x='Catégorie', y='Valeur', title="Graphique dynamique")
    return fig

# Lancer le serveur Dash
if __name__ == '__main__':
    app.run_server(debug=True)
