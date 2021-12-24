import dash
from dash import dcc, html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

from kernels import *

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    #Squared exponential kernel
    html.Div(
        dash.html.H1("Squared exponential kernel"),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

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

    html.Br(),
    html.Div(
        html.Div(dcc.Graph(id='my-output'),
        style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Img(src=app.get_asset_url('img/SEQ.png'),
        style={'width':'50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),


    #Orstein Uhlenbeck kernel
    html.Div(
        dash.html.H1("Orstein Uhlenbeck kernel"),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-OUK', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-OUK',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=3,
                value=2,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Br(),
    html.Div(
        html.Div(dcc.Graph(id='my-output-OUK'),
        style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),
    
    html.Div(
        html.Img(src=app.get_asset_url('img/OUk.png'),
        style={'width':'50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    #Rational quadratic kernel
    html.Div(
        dash.html.H1("Rational quadratic kernel"),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-RQK1', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-RQK1',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-RQK2', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-RQK2',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-RQK3', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-RQK3',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Br(),
    html.Div(
        html.Div(dcc.Graph(id='my-output-RQK1'),
        style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),
    
    html.Div(
        html.Img(src=app.get_asset_url('img/RQK.png'),
        style={'width':'50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    #Periodic kernel
    html.Div(
        dash.html.H1("Periodic kernel"),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-PK1', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-PK1',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-PK2', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-PK2',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-PK3', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-PK3',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Br(),
    html.Div(
        html.Div(dcc.Graph(id='my-output-PK1'),
        style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),
    
    html.Div(
        html.Img(src=app.get_asset_url('img/PK.png'),
        style={'width':'50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    #Polynomial kernel
    html.Div(
        dash.html.H1("Polynomial kernel"),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-PPK1', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-PPK1',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-PPK2', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-PPK2',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-PPK3', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-PPK3',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Div(
        html.Div(
            id='updatemode-output-container-PPK4', 
        style={'margin-top': 5}),
    style={ 'display': 'flex', 'margin': '0px 25% 0px 25%'}),

    html.Div(
        html.Div(
            dcc.Slider(
                id='slider-updatemode-PPK4',
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                max=4,
                value=1,
                step=0.01,
                updatemode='drag'
            ),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Br(),
    html.Div(
        html.Div(dcc.Graph(id='my-output-PPK1'),
        style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),
    
    html.Div(
        html.Img(src=app.get_asset_url('img/PPK.png'),
        style={'width':'50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

])





@app.callback(
    Output('my-output','figure'),
    Input('slider-updatemode', 'value'))
def Squared_exponential_kernel_fig(Input):

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
    return 'l: {} (sigma = 1/l)'.format(value)

@app.callback(
    Output('my-output-OUK','figure'),
    Input('slider-updatemode-OUK', 'value'))
def Orstein_Uhlenbeck_kernel_fig(Input):

    X_k = np.arange(-4,4,0.5).reshape(-1, 1)
    l = Input
    K1 = Orstein_Uhlenbeck_kernel(X_k, X_k, l)

    df = data_3dplot(X_k,K1)

    fig = px.scatter_3d(df, x='x', y='y', z='z')
    return fig

@app.callback(
    Output('updatemode-output-container-OUK', 'children'),
    Input('slider-updatemode-OUK', 'value'))
def update_output_OUK(value):
    return 'l: {} (sigma = 1/l)©'.format(value)


@app.callback(
    Output('my-output-RQK1','figure'),
    Input('slider-updatemode-RQK1', 'value'),
    Input('slider-updatemode-RQK2', 'value'),
    Input('slider-updatemode-RQK3', 'value'))
def Rational_quadratic_kernel_fig(Input1,inpu2, input3):

    X_k = np.arange(-4,4,0.5).reshape(-1, 1)
    l, sigma, alpha = Input1, inpu2, input3
    K1 = Rational_quadratic_kernel(X_k, X_k, l, sigma, alpha)

    df = data_3dplot(X_k,K1)

    fig = px.scatter_3d(df, x='x', y='y', z='z')
    return fig

@app.callback(
    Output('updatemode-output-container-RQK1', 'children'),
    Output('updatemode-output-container-RQK2', 'children'),
    Output('updatemode-output-container-RQK3', 'children'),
    Input('slider-updatemode-RQK1', 'value'),
    Input('slider-updatemode-RQK2', 'value'),
    Input('slider-updatemode-RQK3', 'value'))
def update_output_RQK(l,sigma, alpha):
    return 'l: {}'.format(l),'sigma: {}'.format(sigma),'alpha: {}'.format(alpha)


@app.callback(
    Output('my-output-PK1','figure'),
    Input('slider-updatemode-PK1', 'value'),
    Input('slider-updatemode-PK2', 'value'),
    Input('slider-updatemode-PK3', 'value'))
def Periodic_kernel_fig(Input1,inpu2, input3):

    X_k = np.arange(-4,4,0.5).reshape(-1, 1)
    sigma, p, l = Input1, inpu2, input3
    K1 = Periodic_kernel(X_k, X_k, sigma, p, l)

    df = data_3dplot(X_k,K1)

    fig = px.scatter_3d(df, x='x', y='y', z='z')
    return fig

@app.callback(
    Output('updatemode-output-container-PK1', 'children'),
    Output('updatemode-output-container-PK2', 'children'),
    Output('updatemode-output-container-PK3', 'children'),
    Input('slider-updatemode-PK1', 'value'),
    Input('slider-updatemode-PK2', 'value'),
    Input('slider-updatemode-PK3', 'value'))
def update_output_PK(l,sigma, alpha):
    return 'sigma: {}'.format(l),'p: {}'.format(sigma),'l: {}'.format(alpha)


@app.callback(
    Output('my-output-PPK1','figure'),
    Input('slider-updatemode-PPK1', 'value'),
    Input('slider-updatemode-PPK2', 'value'),
    Input('slider-updatemode-PPK3', 'value'),
    Input('slider-updatemode-PPK4', 'value'))
def Polynomial_kernel_fig(Input1,inpu2, input3, input4):

    X_k = np.arange(-4,4,0.5).reshape(-1, 1)

    sigmab, sigmav, mu, alpha = Input1, inpu2, input3, input4
    K1 = Polynomial_kernel(X_k, X_k, sigmab, sigmav, mu, alpha)

    df = data_3dplot(X_k,K1)

    fig = px.scatter_3d(df, x='x', y='y', z='z')
    return fig

@app.callback(
    Output('updatemode-output-container-PPK1', 'children'),
    Output('updatemode-output-container-PPK2', 'children'),
    Output('updatemode-output-container-PPK3', 'children'),
    Output('updatemode-output-container-PPK4', 'children'),
    Input('slider-updatemode-PPK1', 'value'),
    Input('slider-updatemode-PPK2', 'value'),
    Input('slider-updatemode-PPK3', 'value'),
    Input('slider-updatemode-PPK4', 'value'))
def update_output_PK(sigmab, sigmav, mu, alpha):
    return 'sigmab: {}'.format(sigmab),'sigmav: {}'.format(sigmav),'mu: {}'.format(mu),'alpha: {}'.format(alpha)


if __name__ == '__main__':
    app.run_server(debug=True)