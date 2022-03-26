from dash import Dash, html, dcc, html, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#import flask

#server = flask.Flask(__name__)
#app = Dash(__name__, server=server, url_base_pathname='/dash/')

app = Dash(__name__)

df1 = pd.read_csv('radar.csv')
col = ['acousticness', 'danceability', 'energy', 'duration_ms', 'instrumentalness', 'valence', 'tempo', 'liveness', 'loudness', 'speechiness', 'mode', 'explicit', 'key']
l1 = []
l2 = []
len1 = len(col)
for j in range(10):
    l1 = l1 + col
    for i in range(len1):
        l2.append(df1[col[i]][j])

app.layout = html.Div([
    html.Div([
        dcc.Checklist(
            ['1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s'],
            ['2010s'],
            inline=True,
            id='checkboxs'
    )], style={'postion': 'relative', 'margin': '0 auto', 'height': 'auto', 'text-align':'center', 'clear':'left'}),
    html.Div([
        dcc.Graph(
            id='graph',
            responsive=True,
            style={
            'width':'100%',
            'height':'100%'}
        )
    ], style={'postion': 'relative', 'margin': '0 auto', 'height': 'auto', 'text-align':'center', 'clear':'left'})
])

@app.callback(Output('graph', 'figure'), Input('checkboxs', 'value'))
def update_figure(values):
    fig = go.Figure()
    colors = px.colors.qualitative.Plotly
    for value in values:
        v = (int(value[:4]) - 1920) // 10
        fig.add_trace(go.Scatterpolar(
            r=l2[v * 13: (v + 1) * 13],
            theta=col,
            fill='toself',
            name=value
        ))
    fig.update_polars(radialaxis=dict(range=[-5, 5]))
    fig.update_layout(showlegend=True)
    fig.update_layout(legend=dict(yanchor="top", y=1, xanchor="right", x=0.7))
    return fig


#@server.route('/')
#def index():
#    return '''
#<html>
#<div>
#    <h1>Flask App</h1>
#</div>
#</html>
#'''
#freezer = Freezer(server)

if __name__ == "__main__":
    app.run_server(debug=True)
    #freezer.freeze()
    #freezer.run()
    
