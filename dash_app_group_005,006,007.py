import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

path_of_file = r"D:\NIBM\HNDS\Interactive DB\App_Project_005,006,007\WorldHappiness_Corruption_2015_2020.csv"
data = pd.read_csv(path_of_file)

data['Year'] = data['Year'].astype(str)

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Global Happiness and Corruption Analysis  Dashboard"

# Start
app.layout = html.Div(
    style={'font-family': 'Arial, sans-serif', 'background-color': '#f4f4f4', 'padding': '20px'},
    children=[
        # Header
        html.Div([
            html.H1("🌍 Global Happiness and Corruption Analysis Dashboard", style={'text-align': 'center', 'color': '#333'}),
            html.P(
                "Explore the happiness scores and socio-economic factors influencing happiness across the globe.",
                style={'text-align': 'center', 'font-size': '16px', 'color': '#555'}
            )
        ]),

        # Start Tabs
        dcc.Tabs(id='tabs', value='tab1', children=[
            # Tab 1: Overview
            dcc.Tab(label='Overview', value='tab1', style={'font-weight': 'bold'}, children=[
                html.Div([
                    html.H2("Welcome to the Global Happiness and Corruption Analysis Dashboard!", style={'text-align': 'center'}),
                    html.Img(src='https://www.wellnessfoundation.it/wp-content/uploads/2023/05/highlight-62_page-0001.jpg', style={'display': 'block', 'margin': '20px auto', 'width': '50%'}),
                    html.P("This app provides visual insights into global happiness scores and factors that influence them, such as GDP, health, freedom, and more.",
                           style={'text-align': 'center', 'margin-top': '20px', 'font-size': '16px'})
                ])
            ]),

            # Tab 2: Bar Chart
            dcc.Tab(label='Bar Chart', value='tab2', children=[
                html.Div([
                    html.Label("Select Year:", style={'font-weight': 'bold', 'color': '#333'}),
                    dcc.Dropdown(
                        id='bar_year_dropdown',
                        options=[{'label': year, 'value': year} for year in sorted(data['Year'].unique())],
                        value=data['Year'].unique()[0],
                        clearable=False,
                        style={'width': '200px'}
                    ),
                    html.Label("Select Metric:", style={'font-weight': 'bold', 'color': '#333', 'margin-top': '10px'}),
                    dcc.Dropdown(
                        id='bar_metric_dropdown',
                        options=[
                            {'label': 'Happiness Score', 'value': 'happiness_score'},
                            {'label': 'GDP Per Capita', 'value': 'gdp_per_capita'},
                            {'label': 'Health', 'value': 'health'},
                            {'label': 'Freedom', 'value': 'freedom'},
                            {'label': 'Generosity', 'value': 'generosity'},
                            {'label': 'Government Trust', 'value': 'government_trust'}
                        ],
                        value='happiness_score',
                        clearable=False,
                        style={'width': '200px'}
                    ),
                    dcc.Graph(id='bar_chart')
                ])
            ]),

            # Tab 3: Line Charts
            dcc.Tab(label='Line Charts', value='tab3', children=[
                html.Div([
                    html.Label("Select Country:", style={'font-weight': 'bold', 'color': '#333'}),
                    dcc.Dropdown(
                        id='line_country_dropdown',
                        options=[{'label': country, 'value': country} for country in data['Country'].unique()],
                        value=data['Country'].unique()[0],
                        clearable=False,
                        style={'width': '300px'}
                    ),
                    html.Label("Select Metric:", style={'font-weight': 'bold', 'color': '#333', 'margin-top': '10px'}),
                    dcc.Dropdown(
                        id='line_metric_dropdown',
                        options=[
                            {'label': 'Happiness Score', 'value': 'happiness_score'},
                            {'label': 'GDP Per Capita', 'value': 'gdp_per_capita'},
                            {'label': 'Health', 'value': 'health'},
                            {'label': 'Freedom', 'value': 'freedom'},
                            {'label': 'Generosity', 'value': 'generosity'},
                            {'label': 'Government Trust', 'value': 'government_trust'}
                        ],
                        value='happiness_score',
                        clearable=False,
                        style={'width': '300px'}
                    ),
                    dcc.Graph(id='line_chart')
                ])
            ]),

            # Tab 4: Geographical Map
            dcc.Tab(label='Geographical Map', value='tab4', children=[
                html.Div([
                    html.Label("Select Year:", style={'font-weight': 'bold', 'color': '#333'}),
                    dcc.Dropdown(
                        id='map_year_dropdown',
                        options=[{'label': year, 'value': year} for year in sorted(data['Year'].unique())],
                        value=data['Year'].unique()[0],
                        clearable=False,
                        style={'width': '200px'}
                    ),
                    html.Label("Select Metric:", style={'font-weight': 'bold', 'color': '#333', 'margin-top': '10px'}),
                    dcc.Dropdown(
                        id='map_metric_dropdown',
                        options=[
                            {'label': 'Happiness Score', 'value': 'happiness_score'},
                            {'label': 'GDP Per Capita', 'value': 'gdp_per_capita'},
                            {'label': 'Health', 'value': 'health'},
                            {'label': 'Freedom', 'value': 'freedom'},
                            {'label': 'Generosity', 'value': 'generosity'},
                            {'label': 'Government Trust', 'value': 'government_trust'}
                        ],
                        value='happiness_score',
                        clearable=False,
                        style={'width': '200px'}
                    ),
                    dcc.Graph(id='geo_map')
                ])
            ]),

            # Tab 5: Scatter Plot
            dcc.Tab(label='Scatter Plot', value='tab5', children=[
                html.Div([
                    html.Label("Select X-Axis Variable (Fixed):", style={'font-weight': 'bold', 'color': '#333'}),
                    dcc.Dropdown(
                        id='scatter_x_dropdown',
                        options=[
                            {'label': 'Happiness Score', 'value': 'happiness_score'},
                            {'label': 'GDP Per Capita', 'value': 'gdp_per_capita'},
                            {'label': 'Health', 'value': 'health'},
                            {'label': 'Freedom', 'value': 'freedom'}
                        ],
                        value='happiness_score',  
                        clearable=False,
                        style={'width': '300px'}
                    ),
                    html.Label("Select Y-Axis Variable:", style={'font-weight': 'bold', 'color': '#333', 'margin-top': '10px'}),
                    dcc.RadioItems(
                        id='scatter_y_radio',
                        options=[
                            {'label': 'GDP Per Capita', 'value': 'gdp_per_capita'},
                            {'label': 'Health', 'value': 'health'},
                            {'label': 'Freedom', 'value': 'freedom'}
                        ],
                        value='gdp_per_capita',  
                        labelStyle={'display': 'block', 'margin-top': '5px'}
                    ),
                    dcc.Graph(id='scatter_plot')
                ])
            ]),

            # Tab 6: Interactive Charts
            dcc.Tab(label='Interactive Charts', value='tab6', children=[
                html.Div([
                    html.Label("Chart 1:", style={'font-weight': 'bold', 'color': '#333'}),
                    dcc.Dropdown(
                        id='interactive_metric1_dropdown',
                        options=[
                            {'label': 'Happiness Score', 'value': 'happiness_score'},
                            {'label': 'GDP Per Capita', 'value': 'gdp_per_capita'},
                            {'label': 'Health', 'value': 'health'},
                            {'label': 'Freedom', 'value': 'freedom'}
                        ],
                        value='happiness_score',
                        clearable=False,
                        style={'width': '300px'}
                    ),
                    dcc.Graph(id='chart1'),
                    html.Label(" Chart 2:", style={'font-weight': 'bold', 'color': '#333', 'margin-top': '20px'}),
                    dcc.Dropdown(
                        id='interactive_metric2_dropdown',
                        options=[
                            {'label': 'Happiness Score', 'value': 'happiness_score'},
                            {'label': 'GDP Per Capita', 'value': 'gdp_per_capita'},
                            {'label': 'Health', 'value': 'health'},
                            {'label': 'Freedom', 'value': 'freedom'}
                        ],
                        value='gdp_per_capita',
                        clearable=False,
                        style={'width': '300px'}
                    ),
                    dcc.Graph(id='chart2')
                ])
            ])
        ])
    ]
)

# Callbacks
@app.callback(
    Output('bar_chart', 'figure'),
    [Input('bar_year_dropdown', 'value'),
     Input('bar_metric_dropdown', 'value')]
)
def update_bar_chart(selected_year, selected_metric):
    filtered_data = data[data['Year'] == selected_year]
    bar_chart = px.bar(
        filtered_data,
        x='Country',
        y=selected_metric,
        color='continent',
        title=f'{selected_metric.replace("_", " ").title()} by Country',
        labels={selected_metric: selected_metric.replace("_", " ").title(), 'Country': 'Country'},
        template='plotly_dark'
    )
    bar_chart.update_layout(title_font_size=18, title_x=0.5)
    return bar_chart

@app.callback(
    Output('line_chart', 'figure'),
    [Input('line_country_dropdown', 'value'),
     Input('line_metric_dropdown', 'value')]
)
def update_line_chart(selected_country, selected_metric):
    filtered_data = data[data['Country'] == selected_country]
    line_chart = px.line(
        filtered_data,
        x='Year',
        y=selected_metric,
        title=f'{selected_metric.replace("_", " ").title()} Over Years - {selected_country}',
        labels={selected_metric: selected_metric.replace("_", " ").title(), 'Year': 'Year'},
        markers=True,
        template='plotly_dark'
    )
    line_chart.update_layout(title_font_size=18, title_x=0.5)
    return line_chart

@app.callback(
    Output('geo_map', 'figure'),
    [Input('map_year_dropdown', 'value'),
     Input('map_metric_dropdown', 'value')]
)
def update_geo_map(selected_year, selected_metric):
    filtered_data = data[data['Year'] == selected_year]
    geo_map = px.choropleth(
        filtered_data,
        locations='Country',
        locationmode='country names',
        color=selected_metric,
        hover_name='Country',
        title=f'{selected_metric.replace("_", " ").title()} by Country',
        labels={selected_metric: selected_metric.replace("_", " ").title()},
        template='plotly_dark'
    )
    geo_map.update_layout(title_font_size=18, title_x=0.5)
    return geo_map

@app.callback(
    Output('scatter_plot', 'figure'),
    [Input('scatter_x_dropdown', 'value'),
     Input('scatter_y_radio', 'value')]
)
def update_scatter_plot(x_axis, y_axis):
 
    correlation = data[x_axis].corr(data[y_axis])

    scatter_plot = px.scatter(
        data,
        x=x_axis,
        y=y_axis,
        color='continent',
        title=f'{x_axis.replace("_", " ").title()} vs {y_axis.replace("_", " ").title()} (Correlation: {correlation:.2f})',
        labels={x_axis: x_axis.replace("_", " ").title(), y_axis: y_axis.replace("_", " ").title()},
        template='plotly_dark'
    )
    scatter_plot.update_layout(title_font_size=18, title_x=0.5)
    return scatter_plot

# Callback for Chart 1
@app.callback(
    Output('chart1', 'figure'),
    [Input('interactive_metric1_dropdown', 'value')]
)
def update_chart1(selected_metric):
    # Create a scatter plot for Chart 1
    fig = px.scatter(
        data,
        x='happiness_score',
        y=selected_metric,
        color='continent',
        title=f'Happiness Score vs {selected_metric.replace("_", " ").title()}',
        labels={'happiness_score': 'Happiness Score', selected_metric: selected_metric.replace("_", " ").title()},
        template='plotly_dark',
        custom_data=['Country']  
    )
    fig.update_layout(title_font_size=18, title_x=0.5)
    return fig

# Callback for Chart 2
@app.callback(
    Output('chart2', 'figure'),
    [Input('chart1', 'hoverData'),
     Input('interactive_metric2_dropdown', 'value')]
)
def update_chart2(hoverData, selected_metric):
    if hoverData is None:
        return px.scatter(
            data,
            x='happiness_score',
            y=selected_metric,
            color='continent',
            title=f'Happiness Score vs {selected_metric.replace("_", " ").title()}',
            labels={'happiness_score': 'Happiness Score', selected_metric: selected_metric.replace("_", " ").title()},
            template='plotly_dark'
        )
    

    try:
        country = hoverData['points'][0]['customdata'][0]  
    except (KeyError, IndexError):
    
        return px.scatter(
            data,
            x='happiness_score',
            y=selected_metric,
            color='continent',
            title=f'Happiness Score vs {selected_metric.replace("_", " ").title()}',
            labels={'happiness_score': 'Happiness Score', selected_metric: selected_metric.replace("_", " ").title()},
            template='plotly_dark'
        )
    
    
    filtered_data = data[data['Country'] == country]
    
    fig = px.scatter(
        filtered_data,
        x='happiness_score',
        y=selected_metric,
        color='continent',
        title=f'Happiness Score vs {selected_metric.replace("_", " ").title()} for {country}',
        labels={'happiness_score': 'Happiness Score', selected_metric: selected_metric.replace("_", " ").title()},
        template='plotly_dark'
    )
    fig.update_layout(title_font_size=18, title_x=0.5)
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=1234)
