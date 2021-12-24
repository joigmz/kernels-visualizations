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
        dash.html.H1("Squared exponential kernel"),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=3,
                value=2,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Br(),
    html.Div(
        html.Div(dcc.Graph(id='my-output'),
        style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),
    html.Hr(),
])

@app.callback(
    Output('my-output','figure'),
    Input('slider-updatemode', 'value'))
def update_output_div(Input):

    X_k = np.arange(-4,4,0.5).reshape(-1, 1)
    l = Input
    K1 = Squared_exponential_kernel(X_k, X_k, l)

    df = data_3dplot(X_k,K1)

    fig = px.scatter_3d(df, x='x', y='y', z='z')
    return fig

@app.callback(
    Output('updatemode-output-container', 'children'),
    Input('slider-updatemode', 'value'))
def update_output(value):
    return 'l: {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)