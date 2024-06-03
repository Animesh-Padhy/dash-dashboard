import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd 
import plotly.express as px

df = pd.read_csv('../data/gapminderDataFiveYear.csv')

continents = df['continent'].unique()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('Life Expectancy vs. GDP per Capita',style = {'backgroundColor': '#385170', 'color':'#ececec','margin':0,'padding': '10px'}),
    
    dbc.Row([
        dbc.Col([
            dbc.Label("Select Continent"),
            dcc.Dropdown(
                id="continent-dropdown",
                options=[
                    {"label": continent, "value": continent}
                    for continent in continents
                ],
                value="Americas"  
            )
        ], width=6),
        dbc.Col([
            dbc.Label("Select Year"),
            dcc.Dropdown(
                id="year-dropdown",
                options=[
                    {"label": str(year), "value": year}
                    for year in df["year"].unique()
                ],
                value=1972  
            )
        ], width=6)
    ], style={'backgroundColor': '#385170', 'color':'#ececec', 'padding': '20px', 'borderRadius': '5px'}),
    html.H3(id='header-text'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='scatter-plot')
        ], width=12)
    ])
], fluid=True)


@app.callback(
    Output("scatter-plot", 'figure'),
    [Input('continent-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_scatter_plot(selected_continent, selected_year):
    if not selected_continent or not selected_year:
        return {}

    filtered_df = df[(df["continent"] == selected_continent) & (df["year"] == selected_year)]
    fig = px.scatter(
        filtered_df, x="gdpPercap", y="lifeExp", color="country",
        title=f"Life Expectancy vs GDP per Capita in {selected_continent} ({selected_year})",
        labels={"gdpPercap": "GDP per Capita", "lifeExp": "Life Expectancy"},
        size_max=20  
    )
    return fig

@app.callback(
    Output('header-text', 'children'),
    [Input('continent-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_header(selected_continent, selected_year):
    if not selected_continent or not selected_year:
        return "Please select a continent and a year"

    header_text = f"{selected_continent} - Life Expectancy vs. GDP per Capita ({selected_year})"
    return header_text

if __name__ == '__main__':
    app.run_server(debug=True)
