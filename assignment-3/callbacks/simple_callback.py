import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd 
import plotly.express as px

df = pd.read_csv('../data/gapminderDataFiveYear.csv')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('GDP in Different Countries of the World from 1952 to 2007'),
    dbc.Row([
        dbc.Col([
            dbc.Label("Select Countries"),
            dcc.Dropdown(
                id="country-dropdown",
                options=[
                    {"label": country, "value": country}
                    for country in df["country"].unique()
                ],
                value=["Canada"],  # Default value
                multi=True  # Allow multiple selections
            )
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='gdp-pie-chart')
        ], width=12)
    ])
], fluid=True)

@app.callback(
    Output("gdp-pie-chart", 'figure'),
    [Input('country-dropdown', 'value')]
)

def update_pie_chart(selected_countries):
    if not selected_countries:
        return {}

    filtered_df = df[df["country"].isin(selected_countries) & (df["year"] == 2007)]
    fig = px.pie(
        filtered_df, values="gdpPercap", names="country",
        title="GDP per Capita (2007)",
        labels={"gdpPercap": "GDP per Capita"}
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
