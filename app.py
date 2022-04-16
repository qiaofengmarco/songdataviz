from dash import Dash, html, dcc, html, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from pages import radar, decates

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

nav_item1 = dbc.NavItem(dbc.NavLink("Big Picture", href="/radar", id="link1", className="links"))
nav_item2 = dbc.NavItem(dbc.NavLink("Decates", href="/decates", id="link2", className="links"))

default = dbc.NavbarSimple(
    children=[nav_item1, nav_item2],
    brand="CS 5346 Group 10",
    brand_href="#",
    sticky="top",
    className="mb-5",
    color="black",
    dark=True,
)

#custom_default = dbc.Navbar(
#    dbc.Container(
#        [
#            dbc.NavbarBrand("Custom default", href="#"),
#            dbc.NavbarToggler(id="navbar-toggler1"),
#            dbc.Collapse(
#                dbc.Nav(
#                    [nav_item, dropdown], className="ms-auto", navbar=True
#                ),
#                id="navbar-collapse1",
#                navbar=True,
#            ),
#        ]
#    ),
#    className="mb-5",
#)

app.layout = html.Div([
    default,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
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
    else:
        return defaultLayout

if __name__ == "__main__":
    app.run_server(debug=True)
    
