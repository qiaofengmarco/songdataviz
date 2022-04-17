import dash_gif_component as gif
from dash import Dash, html, dcc

layout = html.Div([
    html.H5("Samuel Baber's Music Style", style={'font-family':'Copperplate'}),
    html.Br(),
    html.Div([
        html.Img(
            src='/assets/samuel-baber-face.jpeg'
        ),
        gif.GifPlayer(
            gif='/assets/samuel-baber.gif',
            still='/assets/samuel1.png',
        )
    ],style={
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
    }),
    html.Div([
        html.Br(),
        html.P("Samuel Barber is a famous musician born in America (the left figure is his portrait). As shown in the right figure, Samuel's music style can be roughly divided into 4 phases.", style={'text-align':'left'}),
        html.P("Before 1936, his music had high score in instrumentalness and moderate score in loudness, danceability and valence. After 1937, he had a sharp decrease in instrumentalness and valence, suggesting his music were conveying bad tempos during this period. In 1951, his scores were steady and average. After 1955, Samuel suddenly went to an extreme: with super low score in valence, loudness, energy and danceability. This style changing is consistent with Samuel's life experience.",style={'text-align':'left'}),
        html.P("According to Wikipedia, during his youth (1928 to 1940), Samuel was dedicated in depicting his childhood and was identified for the use of unresolved chromaticism and dissonance. In his mid career, he cooperated with several symphonies in classic music and his style became more moderate. After the second world war, Samuel served in US Air Corps for a while and wrote symphony for US Air Forces. In his late career, Samuel had a harsh life. His works were rejected for several times. He got in depression and alcoholism, making his music unstable.", style={'text-align':'left'})
    ], style={
        'margin': 'auto 5%',
        'align': 'left'
    })
])
