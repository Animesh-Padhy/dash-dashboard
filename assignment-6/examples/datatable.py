import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd 
import plotly.express as px
import plotly.graph_objs as go

df = pd.read_csv('data/gapminderDataFiveYear.csv')

df['id'] = df.index


df_2007 = df[df['year'] == 2007][['country', 'continent', 'lifeExp', 'pop', 'gdpPercap', 'id']]


colors = {
    'lifeExp': '#636EFA',
    'pop': '#EF553B',
    'gdpPercap': '#00CC96'
}


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('2007 Gapminder Data', style={'backgroundColor': '#f8f9fa', 'padding': '10px'}),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='table',
                columns=[
                    {"name": col, "id": col} for col in ['country', 'continent', 'lifeExp', 'pop', 'gdpPercap']
                ],
                data=df_2007.to_dict('records'),
                style_data_conditional=[
                    {'if': {'column_id': 'lifeExp'}, 'backgroundColor': colors['lifeExp'], 'color': 'white'},
                    {'if': {'column_id': 'pop'}, 'backgroundColor': colors['pop'], 'color': 'white'},
                    {'if': {'column_id': 'gdpPercap'}, 'backgroundColor': colors['gdpPercap'], 'color': 'white'},
                ],
                style_table={'overflowX': 'auto'},
                row_selectable='single',
                selected_cells=[{"row": 0, "column": 0, "column_id": "country", "row_id": 0}],
                active_cell={"row": 0, "column": 0, "column_id": "country", "row_id": 0},
                page_action = 'native',
                page_size = 10
            ),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='line-chart')
        ], width=6)
    ])
], fluid=True)

@app.callback(
    Output("line-chart", 'figure'),
    [Input('table', 'active_cell')]
)
def update_line_chart(active_cell):
    if active_cell is None:
        return go.Figure()

    
    row_id = active_cell['row_id']
    selected_country = df_2007.iloc[row_id]['country']
    
    
    country_data = df[df['country'] == selected_country]
    
    
    column_id = active_cell['column_id']
    variable = column_id if column_id in ['lifeExp', 'pop', 'gdpPercap'] else 'lifeExp'
    
    fig = px.line(
        country_data, x='year', y=variable,
        title=f'{selected_country} - {variable} over Time',
        labels={variable: variable, 'year': 'Year'},
        markers=True
    )
    
    fig.update_traces(marker=dict(size=12)) 
    fig.update_layout(yaxis=dict(title=variable, tickfont=dict(size=14)))
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
