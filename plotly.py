# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
print( min_payload,"afafafsa" , spacex_df.columns)
# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                    options=[{'label': 'All Sites', 'value': 'ALL'},
                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                        value='ALL',
                                        placeholder='All Sites',
                                        searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(
                                    id = 'payload-slider',
                                    min = 0,
                                    max = 10000,
                                    step = 1000,
                                    value = [min_payload,max_payload]

                                ),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
            Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filter_df = spacex_df.groupby("Launch Site").sum()['class'].to_frame().reset_index()
    if entered_site == 'ALL':
        fig = px.pie(data_frame=filter_df,
                names='Launch Site',
                values='class',
                title='Total Success Launches By Site')
        return fig
    if entered_site == 'CCAFS LC-40':
        filter_df = spacex_df[spacex_df['Launch Site']=='CCAFS LC-40']["class"].value_counts().reset_index()
        fig = px.pie(data_frame=filter_df,
                names='index',
                values='class',
                title='Total Success Launches By Site CCAFS LC-40')
        return fig
    if entered_site == 'VAFB SLC-4E':
        filter_df = spacex_df[spacex_df['Launch Site']=='VAFB SLC-4E']["class"].value_counts().reset_index()
        fig = px.pie(data_frame=filter_df,
                names='index',
                values='class',
                title='Total Success Launches By Site VAFB SLC-4E')
        return fig
    if entered_site == 'KSC LC-39A':
        filter_df = spacex_df[spacex_df['Launch Site']=='KSC LC-39A']["class"].value_counts().reset_index()
        fig = px.pie(data_frame=filter_df,
                names='index',
                values='class',
                title='Total Success Launches By Site KSC LC-39A')
        return fig
    if entered_site == 'CCAFS SLC-40':
        filter_df = spacex_df[spacex_df['Launch Site']=='CCAFS SLC-40']["class"].value_counts().reset_index()
        fig = px.pie(data_frame=filter_df,
                names='index',
                values='class',
                title='Total Success Launches By Site CCAFS SLC-40')
        return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
            [Input(component_id='site-dropdown', component_property='value'), 
            Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site, payload_value):
    filter_df = spacex_df[["Payload Mass (kg)","class",'Booster Version Category']]
    if entered_site == 'ALL':
        fig = px.scatter(data_frame=filter_df,
                x='Payload Mass (kg)',
                y='class',
                color='Booster Version Category',
                title='Correlation between Payload and Success for all Sites')
        return fig
    if entered_site == 'CCAFS LC-40':
        filter_df = spacex_df[spacex_df['Launch Site']=='CCAFS LC-40'][["Payload Mass (kg)","class",'Booster Version Category']]
        fig = px.scatter(data_frame=filter_df,
                x='Payload Mass (kg)',
                y='class',
                color='Booster Version Category',
                title='Correlation between Payload and Success for CAFS LC-40')
        return fig
    if entered_site == 'VAFB SLC-4E':
        filter_df = spacex_df[spacex_df['Launch Site']=='VAFB SLC-4E'][["Payload Mass (kg)","class",'Booster Version Category']]
        fig = px.scatter(data_frame=filter_df,
                x='Payload Mass (kg)',
                y='class',
                color='Booster Version Category',
                title='Correlation between Payload and Success for VAFB SLC-4E')
        return fig
    if entered_site == 'KSC LC-39A':
        filter_df = spacex_df[spacex_df['Launch Site']=='KSC LC 39A'][["Payload Mass (kg)","class",'Booster Version Category']]
        fig = px.scatter(data_frame=filter_df,
                x='Payload Mass (kg)',
                y='class',
                color='Booster Version Category',
                title='Correlation between Payload and Success for KSC LC 39A')
        return fig
    if entered_site == 'CCAFS SLC-40':
        filter_df = spacex_df[spacex_df['Launch Site']=='CCAFS SLC-40'][["Payload Mass (kg)","class",'Booster Version Category']]
        fig = px.scatter(data_frame=filter_df,
                x='Payload Mass (kg)',
                y='class',
                color='Booster Version Category',
                title='Correlation between Payload and Success for CCAFS SLC-40')
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
