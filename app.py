from dash import Dash, html, dcc, html, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from pages import radar, decates, network, artist

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

nav_item0 = dbc.NavItem(dbc.NavLink("EDA", href="/eda", id="link0", className="links"))
nav_item1 = dbc.NavItem(dbc.NavLink("Radar", href="/radar", id="link1", className="links"))
nav_item2 = dbc.NavItem(dbc.NavLink("Decades", href="/decades", id="link2", className="links"))
nav_item3 = dbc.NavItem(dbc.NavLink("Network", href="/network", id="link3", className="links"))
nav_item4 = dbc.NavItem(dbc.NavLink("Artist", href="/artist", id="link4", className="links"))

default = dbc.NavbarSimple(
    children=[nav_item0, nav_item1, nav_item2, nav_item3, nav_item4],
    brand="NUS CS5346 Group 10",
    brand_href="/",
    sticky="top",
    className="mb-5",
    color="black",
    dark=True,
)

app.layout = html.Div([
    default,
    html.Div([
        dcc.Location(id='url', refresh=False)
    ], style={'display':'none'}),
    html.Div(id='page-content', style={'postion': 'relative', 'width':'100%', 'height': '100%', 'clear':'left', 'margin':'0 auto', 'text-align':'center'})
])

defaultLayout = html.Div([
    html.H1("Welcome!", style={'font-family':'Copperplate'}),
    html.Br(),
    html.P("This project is for NUS CS5346. You are free to explore every visualization through the links above."),
    html.Div([
    html.Img(src='/assets/homepage.jpg', style={'postion': 'relative', 'width':'100%', 'height': '100%', 'text-align':'center', 'clear':'left'})
    ], style={'margin':'auto 20%'})
])

dashboardLayout = html.Iframe(src="https://public.tableau.com/views/Spotify_EDA/Dashboard1?:showVizHome=no&:embed=true",
    style={'position': 'relative', 'text-align':'center', 'height':'90vh', 'width':'100%'})

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/radar':
        return radar.layout
    elif pathname == '/decades':
        return decates.layout
    elif pathname == '/network':
        return network.layout
    elif pathname == '/eda':
        return dashboardLayout
    elif pathname == '/artist':
        return artist.layout
    else:
        return defaultLayout

if __name__ == "__main__":
    app.run_server(debug=True)
    
