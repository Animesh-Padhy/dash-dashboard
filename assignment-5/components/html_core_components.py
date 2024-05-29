import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('Dash Bootstrap and Core Components'),  # Add a comma here
    dbc.Row([
        dbc.Col([
            dbc.Label("Dropdown"),
            dcc.Dropdown(
                id="country-dropdown",
                options=[
                    {"label": country, "value": country}
                    for country in df["country"].unique()
                ],
                value="Canada"
            )
        ], width=6),  # Adjust width if necessary
        dbc.Col([
            dbc.Label("Select Metric"),
            dbc.RadioItems(
                id="metric-radioitems",
                options=[
                    {"label": "Life Expectancy", "value": "lifeExp"},
                    {"label": "GDP per Capita", "value": "gdpPercap"},
                    {"label": "Population", "value": "pop"},
                ],
                value="lifeExp"
            )
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Slider"),
            dcc.Slider(0, 10, 1, value=5)
        ], width=6),  # Adjust width if necessary
        dbc.Col([
            dbc.Label("Text-Input"),
            dbc.Input(
                placeholder='Enter a value...',
                type='text',
                value=''
            )
        ], width=6)
    ])
], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True)
