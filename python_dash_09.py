from dash import Dash
from dash.html import Div, P
from dash import Input as dcc_input
from dash_core_components import Checklist,Dropdown, Graph
from dash.dependencies import Input, Output
from random import randint
app = Dash(__name__)


X = 25
dataAPI= {
    'index': list(range(X)),
    'idosos': [randint(1, 1000) for _ in range(X)],
    'jovens': [randint(1, 1000) for _ in range(X)],
    'adultos': [randint(1, 1000) for _ in range(X)],
}


app.layout = Div(
    children=[
        
        Checklist(
            id = 'meu_check_list',
            options=[
            {'label': 'Idosos', 'value':'idosos'},
            {'label': 'Jovens', 'value':'jovens'},
            {'label': 'Adultos', 'value':'adultos'},

        ], value =['jovens']),

        Dropdown(
            id='meu_dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barra', 'value': 'bar'},
            ],
            value='line'
        ),
        Graph(
            id='meu_grafico',
            config={'displayModeBar': False},
        )
        
    ]
)

@app.callback(

    Output('meu_grafico', 'figure'),

    [
        Input('meu_check_list', 'value'),
        Input('meu_dropdown','value')
    ]
)

def meu_callback(input_data, graph_type):
    grafico={
        'data':[]
    }

    for x in input_data:
        grafico['data'].append(
            {
                'y':dataAPI[x],
                'x':dataAPI['index'],
                'name':x,
                'type':graph_type,
            }
        )
    return grafico

# radando o app
app.run_server(debug=True)


