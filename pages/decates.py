from dash import Dash, html, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('artists.csv')
layout = html.Div([
    html.Div([
        html.Span("Select a decade"),
        dcc.Dropdown(
            ['1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s'],
            '2010s',
            clearable=False,
            id='dropdown'
        )
    ],
    style={
        'width': '20%',
        'height': 'auto',
        'postion': 'relative',
        'margin': '0 auto',
        'height': 'auto',
        'text-align':'center',
        'clear':'left',
        'float':'right'
    }),
    html.Div([
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(id="wctitle")
    ]),
    html.Div([
        html.Br(),
        html.Img(id="image",style={
            'display': 'block',
    #        'max-width':'1200px',
    #        'max-height':'400px',
    #        'width': 'auto',
    #        'height': 'auto',
            'width': '100%',
            'height':'100%',
            'postion': 'relative',
            'margin': '0 auto',
            'height': 'auto',
            'text-align':'center',
            'clear':'left'
        })
    ]),
    html.Div([
        dcc.Graph(
            id='graph1',
            responsive=True,
            style={
            'width':'100%',
            'height':'100%'}
        )
    ], style={'postion': 'relative', 'margin': '0 auto', 'height': 'auto', 'text-align':'center', 'clear':'left'})
])

@callback(Output('image', 'src'), Output('graph1', 'figure'), Output('wctitle', 'children'), Input('dropdown', 'value'))
def update_output(value):
    src = "/assets/wc" + value[:-1] + ".png"
    v = (int(value[:4]) - 1920) // 10
    df1 = df[df['new_col'] == v][['artist', 'popularity']]
    st1 = "Top-20 Popular Artists in " + value
    fig = px.bar(df1, x='artist', y='popularity')
    fig.update_traces(marker_color='lightsteelblue')
    fig.update_layout(title_text=st1, title_x=0.5, title_font_color="black")
    fig.update_layout(hoverlabel_align='right', plot_bgcolor='white', paper_bgcolor='white')
    st2 = "Word Cloud of Song Lyrics in " + value
    
    return src, fig, [html.H5(st2)]
