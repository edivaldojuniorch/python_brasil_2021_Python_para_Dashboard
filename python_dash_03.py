from dash import Dash
from dash.html import Div, H1, H3
from dash_core_components import Graph


# nome do app
app = Dash(__name__)

# Graph
app.layout = Div(
    children=[
        H1('Olá mundo'),
        H3('Estou amando o Python Brasil 2021'),
        Graph(
            figure={
                'data': [
                    {'x':[1,2,3,4], 'y':[3,2,3,4], 
                    'type':'line', 'name':'primeiro'},
                    {'x':[2,3,3,4], 'y':[3,2,3,4], 
                    'type':'bar', 'name':'segundo'},
                    # {'x':[4,5,6,7], 'type':'box', 'name':'segundo'},
                ],
                'layout':{
                    'title':'Lindo'
                }
            }),
        Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {
                        'y': [1,3,4],
                        'labels': ['0','1','2'],
                        'name': 'Maiores',
                        'type':'pie'
                    },
                ],
                'layout': {
                    'title': 'Minha pizza',
                    'paper_bgcolor': '#222225',
                    'titlefont':{
                        'size': 30,
                        'color': '#e8e9ed'
                    },
                    'font':{
                        'size':25,
                        'color': '#e8e9ed'
                        
                        },
                    "height": 700,  # px
                },
            }
            )

    ])
    




# radando o app
app.run_server(debug=True)


