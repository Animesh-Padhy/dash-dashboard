import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Select(
        id="fake-dropdown",
        options=[
            {"label": "Option 1", "value": "1"},
            {"label": "Option 2", "value": "2"},
            {"label": "Option 3", "value": "3"},
        ],
        value="1"
    ),
    html.Div(id="output")
])


if __name__ == '__main__':
    app.run_server(debug=True)



