#######################################################
## Carregando as bibliotecas a serem utilizadas########
#######################################################


from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
from numpy.core.fromnumeric import size
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash  # (version 1.12.0) pip install dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import html,dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from data_generation.simulator_01 import DataSourcereservoir

######################################################
# INSTANCIANDO O SIMULADOR PARA SER EXECUTADO
######################################################


#######################################################
#Definição das cores de fundo de gráfico e de texto
# https://colorswall.com/
#######################################################
colors = {
    'background': '#E5E8E8',#fcecd4',
    'text': '#000000'
}

#######################################################
#Para escolher o melhor tema para o dash é só utilizar o site abaixo
#https://www.bootstrapcdn.com/bootswatch/
#######################################################

runSimulator = dash.Dash(__name__, external_stylesheets = [dbc.themes.SUPERHERO],
                                        # Para responsivilidade para mobile layout
                                        meta_tags=[ {'name': 'viewport',
                                                    'content': 'width=device-width, initial-scale=1.0'}  ] )

#INICIO DA CRIAÇÃO DO LAYOUT DO DASHBOARD
folders = ["images", "simulations_database"]
#Para facilitar imagina o Container como uma matriz                                                    
runSimulator.layout = dbc.Container([

    dbc.Row([
            #Mais informações dessas mudanças
            #https://hackerthemes.com/bootstrap-cheatsheet/
            ##
            dbc.Col( html.H1('LMMP Well Test API',                     # text-primary add cor azul no texto
                        className = 'text-center text-primary, display-2 shadow' , ),  # mb-4 cria espaço entre a row do titulo e a row abaixo,
                            width = 10 ) , #Isso é o tamanho do elemento, Imaginar que inicialmente o Dash tem tamanho 12
                                                        # representa o numero de colunas  que posso usar no texto               
            dbc.Col([
                    dbc.Card(
                        [
                            dbc.CardImg(src="/static/images/LMMP_LOGO.png", top=True),
                            dbc.CardBody(
                                [
                                html.P("LMMP Well test",
                                    className="card text-white bg-primary text-center"),
                                html.P("API que roda o simulador de reservatórios auxiliar a tomada de decisão ",
                                    className="card-text"),    
                                dbc.CardLink(
                                    'LMMP Homepage', href='http://lmmp.mec.puc-rio.br/lmmp/',
                                className='text-left text-info'),
                                ]
                            ),
                        ],
                        style={"width": "17rem"},     
                        )

                ], width = {'size':2, 'order':2 }) #Estamos colocando a ordem para evitar que ele utilize a ordem dos códigos para criar o dash
            ]),

#CRIAÇÃO DE MAIS UMA LINHA EM BRANCO PARA SERVIR DE ESPACO 
    html.Br(children=[]),
    html.Br(children=[]),


dbc.Row([
            #Mais informações dessas mudanças
            #https://hackerthemes.com/bootstrap-cheatsheet/
            ##
            dbc.Col( dcc.Upload(html.Button('Upload File'))) , #Isso é o tamanho do elemento, Imaginar que inicialmente o Dash tem tamanho 12
                                                        # representa o numero de colunas  que posso usar no texto               
            dbc.Col([
                    dbc.Card(
                        [
                            dbc.CardImg(src="/static/images/LMMP_LOGO.png", top=True),
                            dbc.CardBody(
                                [
                                html.P("LMMP Well test",
                                    className="card text-white bg-primary text-center"),
                                html.P("API que roda o simulador de reservatórios auxiliar a tomada de decisão ",
                                    className="card-text"),    
                                dbc.CardLink(
                                    'LMMP Homepage', href='http://lmmp.mec.puc-rio.br/lmmp/',
                                className='text-left text-info'),
                                ]
                            ),
                        ],
                        style={"width": "17rem"},     
                        )

                ], width = {'size':2, 'order':2 }) #Estamos colocando a ordem para evitar que ele utilize a ordem dos códigos para criar o dash
            ]),

],fluid = True) # para dar um respiro entre as bordas


if __name__ == '__main__':
    runSimulator.run_server(debug=True, port=8000)