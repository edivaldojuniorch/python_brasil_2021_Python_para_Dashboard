from dash import Dash
from dash.html import Div, H1, H3
from dash_core_components import Graph, Dropdown, Slider, Checklist


# nome do app
app = Dash(__name__)

# Graph
app.layout = Div(
    children=[
        H1('Olá mundo'),
        H3('Estou amando o Python Brasil 2021'),
        
        Dropdown(options=[
            {'label': 'Idosos', 'value':'menores'},
            {'label': 'Jovens', 'value':'jovens'},
            {'label': 'Adultos', 'value':'adultos'},

        ], value ='jovens'),

        Slider(min=0, max=10, step=1, value=5),

        Checklist(options=[
            {'label': 'Idosos', 'value':'menores'},
            {'label': 'Jovens', 'value':'jovens'},
            {'label': 'Adultos', 'value':'adultos'},

        ], value =['jovens'])
 
    ])
    
# radando o app
app.run_server(debug=True)


