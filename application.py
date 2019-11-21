# -*- coding: utf-8 -*-
from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_auth
import gunicorn

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Example'),

    html.Div(children='''
        Dashboard.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [6, 5, 4], 'type': 'bar', 'name': 'A'},
                {'x': [1, 2, 3], 'y': [3, 10, 10], 'type': 'bar', 'name': u'B'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

server = app.server

if __name__ == '__main__':
    server.run(debug=True) # , port=80, host='0.0.0.0'

