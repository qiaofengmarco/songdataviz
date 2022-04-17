from dash import Dash, html, dcc, html, Input, Output, callback
import json
import networkx as nx
import plotly.graph_objects as go

G = nx.Graph()
edgs = dict()
with open('edges.txt', 'r') as f:
    edgs = json.load(f)

edges = dict()
for k, v in edgs.items():
    ts = k.split(",")
    edges[(ts[0], ts[1])] = v

record = dict()
with open('nodes.txt', 'r') as f:
    record = json.load(f)

nodes = list(record.keys())
show_nodes = [{"id": n, "label": n, "shape": "dot", "size": 5} for n in nodes]
show_edges = [{"id": start+"_"+end, "from": start, "to": end, "width": v} for (start, end), v in edges.items()]
node_id= dict()
node_id_r = dict()
count = 0
for (start, end), wei in edges.items():
    if wei < 3:
        continue
    if start not in node_id:
        node_id[start] = count
        node_id_r[count] = start
        G.add_node(count, label=start)
        count += 1
    if end not in node_id:
        node_id[end] = count
        node_id_r[count] = end
        G.add_node(count, label=end)
        count += 1
    G.add_edge(node_id[start], node_id[end], weight=wei)
pos = nx.spring_layout(G)
# edges trace
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(color='black', width=1),
    hoverinfo='none',
    showlegend=False,
    mode='lines')

# nodes trace
node_x = []
node_y = []
text = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    text.append(node_id_r[node])

node_trace = go.Scatter(
    x=node_x, y=node_y, text=text, hovertemplate="Artist: %{text}<extra></extra>",
    mode='markers',
    showlegend=False,
    marker=dict(
        color='cornflowerblue',
        size=10,
        line=dict(color='black', width=1)))

# layout
layout = dict(plot_bgcolor='white',
              paper_bgcolor='white',
              margin=dict(t=10, b=10, l=10, r=10, pad=0),
              xaxis=dict(linecolor='white',
                         showgrid=False,
                         showticklabels=False,
                         mirror=True),
              yaxis=dict(linecolor='white',
                         showgrid=False,
                         showticklabels=False,
                         mirror=True))
# figure
fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
fig.update_layout(hoverlabel_font_color="white")

layout = html.Div([
    html.H5("Network of Artists with 40+ Songs"),
    dcc.Graph(
            id='graph',
            figure=fig,
            responsive=True,
            style={
            'position': 'relative',
            'height':'80vh'
            }
    )
])

    
