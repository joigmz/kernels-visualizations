import dash
from dash import dcc, html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

from kernels import *

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div(
        html.Div(dcc.Dropdown(
            id="Dropdown-symbols",
            options=[
            {'label': i, 'value': i} for i in range(1,10,1)
            ],
            value=1),
            style={'width': '50%'}),
        style={ 'display': 'flex', 'justify-content': 'center'}),
    html.Br(),
    html.Div(
        html.Div(dcc.Graph(id='my-output'),
        style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),
])
@app.callback(
    Output('my-output','figure'),
    Input('Dropdown-symbols', 'value'))

def update_output_div(Input):

    X_k = np.arange(-4,4,0.5).reshape(-1, 1)
    l = Input
    K1 = Squared_exponential_kernel(X_k, X_k, l)

    xs,ys = [],[]
    zs1 = []

    for i in range(K1.shape[0]):
        for j in range(K1.shape[1]):
            xs.append(X_k[i][0])
            ys.append(X_k[j][0])
            zs1.append(K1[i,j])

    df = pd.DataFrame(np.array([xs,ys,zs1]).T, columns = ['x','y','z'])

    fig = px.scatter_3d(df, x='x', y='y', z='z')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)