# 3. Make a clean UI with a navbar and filters to filter out data based on "type" and "group".
# The change of filters should reflect in the graphs live.
# MANIS SAHA

import dash
from dash import dcc, html, Input, Output
import requests
import plotly.graph_objs as go
import time


# Fetch data from the API
def fetch_data():
    url = "https://random-data-api.com/api/v2/blood_types?size=100&response_type=json"
    retries = 5  # Number of retries
    delay = 1  # Initial delay in seconds

    for _ in range(retries):
        response = requests.get(url)

        # Check response status code
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except Exception as e:
                print(f"Error decoding JSON: {e}")
                return None
        elif response.status_code == 429:  # Too many requests
            print("Too many requests. Retrying after delay...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
        else:
            print(f"Failed to fetch data: Status code {response.status_code}")
            return None

    print("Max retries exceeded. Could not fetch data.")
    return None


# Initialize Dash app
app = dash.Dash(__name__)

# Fetch initial data
initial_data = fetch_data()

# Define the layout of the app
app.layout = html.Div([
    html.Nav([
        html.Div([
            html.H1("Blood Type Data"),
            dcc.Dropdown(
                id='type-dropdown',
                options=[{'label': t, 'value': t} for t in set([entry['type'] for entry in initial_data])],
                value=None,
                placeholder="Select type"
            ),
            dcc.Dropdown(
                id='group-dropdown',
                options=[{'label': g, 'value': g} for g in set([entry['group'] for entry in initial_data])],
                value=None,
                placeholder="Select group"
            ),
        ], className="container")
    ]),
    dcc.Graph(id='blood-type-graph')
])


# Define callback to update graph based on filters
@app.callback(
    Output('blood-type-graph', 'figure'),
    [Input('type-dropdown', 'value'),
     Input('group-dropdown', 'value')]
)
def update_graph(selected_type, selected_group):
    filtered_data = initial_data

    if selected_type:
        filtered_data = [entry for entry in filtered_data if entry['type'] == selected_type]

    if selected_group:
        filtered_data = [entry for entry in filtered_data if entry['group'] == selected_group]

    # Count occurrences of each blood type
    blood_type_counts = {}
    for entry in filtered_data:
        blood_type = entry['type']
        blood_type_counts[blood_type] = blood_type_counts.get(blood_type, 0) + 1

    # Create bar chart
    x_values = list(blood_type_counts.keys())
    y_values = list(blood_type_counts.values())

    trace = go.Bar(
        x=x_values,
        y=y_values
    )

    layout = go.Layout(
        title='Blood Type Distribution',
        xaxis=dict(title='Blood Type'),
        yaxis=dict(title='Count')
    )

    return {'data': [trace], 'layout': layout}


if __name__ == '__main__':
    app.run_server(debug=True)
