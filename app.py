from dash import Dash, html, dcc, html, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from pages import radar, decates, network

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

nav_item1 = dbc.NavItem(dbc.NavLink("Big Picture", href="/radar", id="link1", className="links"))
nav_item2 = dbc.NavItem(dbc.NavLink("Decates", href="/decates", id="link2", className="links"))
nav_item3 = dbc.NavItem(dbc.NavLink("Network", href="/network", id="link3", className="links"))

default = dbc.NavbarSimple(
    children=[nav_item1, nav_item2, nav_item3],
    brand="NUS CS5346 Group 10",
    brand_href="/",
    sticky="top",
    className="mb-5",
    color="black",
    dark=True,
)

app.layout = html.Div([
    default,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', style={'postion': 'relative', 'width':'100%', 'height': '100%', 'text-align':'center', 'clear':'left'})
])

defaultLayout = html.Div([
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/radar':
        return radar.layout
    elif pathname == '/decates':
        return decates.layout
    elif pathname == '/network':
        return network.layout
    else:
        return defaultLayout

if __name__ == "__main__":
    app.run_server(debug=True)
    
