from dash import Dash, dcc, html  # Updated imports (Dash 2.0+)

# Create a Dash application
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data': [  # lowercase 'data' (not 'Data')
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'chart'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'Line chart'},
                ],
                'layout': {
                    'title': 'Graph title',
                    'xaxis': {'title': 'X-axis'},
                    'yaxis': {'title': 'Y-axis'},
                }
            }
        )
    ]
)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)