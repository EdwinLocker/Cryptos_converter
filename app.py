########################################################################################################################
# Project : Tanuki tavern
# Name : Simple dash app with statistics and simple tools for cryptos
# Description : Is used to create the web app with dash components
# Author : Lucas Monachon
########################################################################################################################
from datetime import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import coingecko_rest_service

# make some moves on data
df_coins = pd.DataFrame.from_dict(coingecko_rest_service.get_coins_list())
coins_symbol_list = pd.Series(df_coins["symbol"])


# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]
# external_stylesheets = [dbc.themes.BOOTSTRAP]
# external_stylesheets = [dbc.themes.JOURNAL]
# external_stylesheets = [dbc.themes.SKETCHY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(
            id="coin_selector",
            children=[
                dbc.Container(
                    id='infos_selector',
                    children=[
                        dbc.Card(
                            dbc.Row([
                                dbc.Col([
                                    html.P(
                                        children="Please select a coin you want to check",
                                        className="text-center text-light bg-dark"
                                    ),
                                    dcc.Dropdown(
                                        id="user_selector",
                                        options=[{"label": i, "value": i} for i in coins_symbol_list[:]],
                                    )],
                                    width=4
                                ),
                                dbc.Col([
                                    html.P(
                                        children="Please select a date",
                                        className="text-center text-light bg-dark"
                                    ),
                                    dcc.DatePickerRange(
                                        id='date_picker_range',
                                        style={
                                            'width': '100%',
                                            'paddingLeft': '25px'
                                        },
                                        display_format='DD MM YYYY',
                                        min_date_allowed=dt(2019, 1, 1),  # year, month, day
                                        max_date_allowed=dt(dt.today().year, dt.today().month, dt.today().day+2),
                                    )],
                                    width=4
                                )
                            ]),
                            body=True, color="dark"
                        )
                    ]
                )
            ]
        ),
        html.Hr(),
        html.Div(
            id="power_chart"
        )
    ]
)


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)