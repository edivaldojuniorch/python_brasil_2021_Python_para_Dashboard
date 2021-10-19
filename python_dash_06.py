from dash import Dash
from dash.html import Div, H1, H3
from dash_core_components import Graph, Dropdown, Slider, Checklist

from random import randint

X = 25
dataAPI= {
    'index': list(range(X)),
    'idosos': [randint(1, 1000) for _ in range(X)],
    'jovens': [randint(1, 1000) for _ in range(X)],
    'adultos': [randint(1, 1000) for _ in range(X)],
}

# nome do app
app = Dash(__name__)

# Graph
app.layout = Div(
    children=[
        H1('Olá mundo'),
        H3('Estou amando o Python Brasil 2021'),
        
        Dropdown(options=[
            {'label': 'Idosos', 'value':'idosos'},
            {'label': 'Jovens', 'value':'jovens'},
            {'label': 'Adultos', 'value':'adultos'},

        ], value ='jovens'),

        Slider(min=0, max=10, step=1, value=5),

        Checklist(options=[
            {'label': 'Idosos', 'value':'menores'},
            {'label': 'Jovens', 'value':'jovens'},
            {'label': 'Adultos', 'value':'adultos'},

        ], value =['jovens']),
        Graph(
            figure={
                'data': [
                    {'x':dataAPI['index'], 'y':dataAPI['jovens'],'type':'line', 'name':'primeiro'},
                ],
                'layout':{
                    'title':'Lindo'
                }
            }),
 
    ])
    
# radando o app
app.run_server(debug=True)


