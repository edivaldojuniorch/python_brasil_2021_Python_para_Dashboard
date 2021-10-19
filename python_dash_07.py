from dash import Dash
from dash.html import Div, P
from dash_core_components import Input as dcc_input
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = Div(
    children=[
        dcc_input(
            id='meu_input',
            value = 'Python Brasil'
        ),
        P(
            id='meu_output'
        )
    ]
)

@app.callback(
    Output('meu_output','children'),
    Input('meu_input','value')
)

def meu_callback_nao_citado(meu_input):
    return meu_input

# radando o app
app.run_server(debug=True)


