import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
# Imports all needed libraries
# Importa todas as bibliotecas necessárias


app = dash.Dash()
# Starts the Dash app.
# Inicializa o aplicativo Dash.

dashb_df = pd.read_csv(
    'https://covid19.who.int/WHO-COVID-19-global-data.csv')
# Write the dataset in the variable 'dashb_df' as a DataFrame.
# Atribui o dataset para à variável 'dashb_df' como um DataFrame.

br_dashb_df = dashb_df.loc[dashb_df['Country_code'] == 'BR']
# Select all rows that are from Brazil.
# Seleciona todas as linhas que são do Brasil.

fig = px.bar(
    br_dashb_df,
    x = 'Date_reported',
    y = ['New_cases', 'New_deaths'],
    labels={'Date_reported': 'Data', 'New_deaths': 'Mortes',
            'value':'Quantia',
            'variable':'variáveis'},
    title='Casos de infecção e mortes por Covid'
)
# Defines the graph plot parameters based on the br_dash_df data.
# Define os paramentros de plotagem do gráfico com base nos dados do br_dash_df.

app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])
# Defines a basic html application that will render the dashboard
# Define uma aplicação básica de html que irá renderizar o dashboard

if __name__ == "__main__":
    app.run_server(debug=True)
# Host the application in a local server
# Hospeda a aplicação em um servidor local