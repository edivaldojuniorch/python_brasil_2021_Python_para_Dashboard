from dash import Dash
from dash.html import Div, H1, H3


# nome do app
app = Dash(__name__)

# layout
app.layout = Div(
    children=[
        H1('Olá mundo'),
        H3('Estou amando o Python Brasil 2021')
    
    ])
    
# radando o app
app.run_server(debug=True)


