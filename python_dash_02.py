from dash import Dash
from dash_core_components import Graph


# nome do app
app = Dash(__name__)

# Graph
app.layout = Graph(
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
    },
    
)
# radando o app
app.run_server(debug=True)


