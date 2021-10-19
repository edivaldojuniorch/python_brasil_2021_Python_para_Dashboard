from dash import Dash
from dash.html import Div, P
from dash_core_components import Input as dcc_input
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = Div(
    children=[
        dcc_input(
            id='meu_input_1',
            value = 'Python Brasil'
        ),
        dcc_input(
            id='meu_input_2',
            value = 'Python Brasil'
        ),
        P(id='meu_output_1'),
        P(id='meu_output_2')
        
    ]
)

@app.callback(
    [Output('meu_output_1','children'),Output('meu_output_2','children')],
    [Input('meu_input_1','value'), Input('meu_input_2','value')]
)

def meu_callback_nao_citado(meu_input_1,meu_input_2):
    return meu_input_2, meu_input_1

# radando o app
app.run_server(debug=True)


