#######################################################
## Carregando as bibliotecas a serem utilizadas########
#######################################################


from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
from numpy.core.fromnumeric import size
import datetime
import base64
import io
import pandas as pd
import plotly.express as px 
# import dash_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash  # (version 1.12.0) pip install dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import html,dcc,dash_table
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
#CRIAÇÃO DA PRIMEIRA LINHA COM OS COMPONENTES PARA PARA COMANDAR O SIMULADOR
    dbc.Row([
        
        dbc.Col([
            #Action para escolher qual vai ser a permeabilidade da regiao homogenea
                html.H2('Homogeneous Permeability'),
                html.Br(children=[]),
                dcc.Input(
                            id="input_permeab",
                            type="number",
                            placeholder="input [mD]",
                        ),

        ], width = {'size':3, 'order':1 }),

        dbc.Col([
            #Action para escolher qual vai ser a permeabilidade da regiao DO SKIN
                html.H2('Skin Permeability'),
                html.Br(children=[]),
                dcc.Input(
                            id="input_skin_permab",
                            type="number",
                            placeholder="input [mD]",
                        ),

        ], width = {'size':3, 'order':2 }),

        dbc.Col([
            #Action para escolher qual vai ser a reigão filtrada
                html.H2('Time Test'),
                html.Br(children=[]),
                dcc.Input(
                            id="input_total_time",
                            type="number",
                            placeholder="input [Days]",
                        ),

        ], width = {'size':3, 'order':3 }),
        dbc.Col([
            #Action para escolher qual vai ser a reigão filtrada
                html.H2('Flow Time'),
                html.Br(children=[]),
                dcc.Input(
                            id="input_flow_time",
                            type="number",
                            placeholder="input [Days]",
                        ),

        ], width = {'size':3, 'order':4 }),


    ], align="center"),

#CRIAÇÃO DE MAIS UMA LINHA EM BRANCO PARA SERVIR DE ESPACO 
    html.Br(children=[]),
    html.Br(children=[]),

#CRIAÇÃO DA SEGUNDA LINHA COM OS COMPONENTES PARA COMANDAR O SIMULADOR
    dbc.Row([
        
        dbc.Col([
            #Action para escolher qual vai ser a permeabilidade da regiao homogenea
                html.H2('Homogeneous Porosity'),
                html.Br(children=[]),
                dcc.Input(
                            id="input_porosity",
                            type="number",
                            placeholder="input [fraction]",
                        ),

        ], width = {'size':3, 'order':1 }),

        dbc.Col([
            #Action para escolher qual vai ser a reigão filtrada
                html.H2('Skin radius'),
                html.Br(children=[]),
                dcc.Input(
                            id="input_skin_radius",
                            type="number",
                            placeholder="input [m]",
                        ),

        ], width = {'size':3, 'order':2 }),

        dbc.Col([
            #Action para escolher qual vai ser a reigão filtrada
                html.H2('Flow rate'),
                html.Br(children=[]),
                dcc.Input(
                            id="input_flowrate",
                            type="number",
                            placeholder="input [m3/day]",
                        ),

        ], width = {'size':3, 'order':3 }),

        dbc.Col([
            #Action para escolher qual vai ser a reigão filtrada
                # html.H2('Flow rate'),
                html.Br(children=[]),
                dbc.Button("Run the Simulator",id="Run_simulator",color="success", size="lg", className="me-1", n_clicks=None),
                # html.Button("Run the Simulator",id='submit-button-run', n_clicks=0),

        ], width = {'size':3, 'order':4 }),

        
    ], align="center"),

# #CRIAÇÃO DE MAIS UMA LINHA EM BRANCO PARA SERVIR DE ESPACO 
    html.Br(children=[]),
    html.Br(children=[]),
    html.Br(children=[]),
    html.Br(children=[]),

# # #CRIAÇÃO DA SEGUNDA LINHA COM OS COMPONENTES PARA COMANDAR O SIMULADOR
    dbc.Row([
        
        dbc.Col([
            #Action para escolher qual vai ser a permeabilidade da regiao homogenea
                # html.H2('Simulator Status:'),
                # html.Br(children=[]),
                html.Div(id='output-state')

        ], width = {'size':10, 'order':1 }),
    ], align="center"),

dbc.Row([
            #Mais informações dessas mudanças
            #https://hackerthemes.com/bootstrap-cheatsheet/
            ##
            dbc.Col( 
                html.H1('Choose the file to post process',                     # text-primary add cor azul no texto
                        className = 'text-center text-primary, display-2 shadow' , ),  # mb-4 cria espaço entre a row do titulo e a row abaixo,
                        width = {'size':8, 'order':1 } ) , #Isso é o tamanho do elemento, Imaginar que inicialmente o Dash tem tamanho 12
                                                        # representa o numero de colunas  que posso usar no texto

            dbc.Col( dcc.Upload(
                        dbc.Button("Upload file",id="upload_button", color="warning", size="lg", className="me-1",n_clicks=None),id="upload-data",
                        # Allow multiple files to be uploaded
                        multiple=True
                        ),width = {'size':3, 'order':4 }),               
            ], align="center"),
# #CRIAÇÃO DE MAIS UMA LINHA EM BRANCO PARA SERVIR DE ESPACO 
html.Br(children=[]),
html.Br(children=[]),
# html.Br(children=[]),
# # html.Br(children=[]),
#             dbc.Row([
#                     html.Div([html.Div(id='output-data-upload')]),               
#                     ]),
            html.Div([html.Div(id='output-data-upload')],style={'backgroundColor': 'black'}),
html.Br(children=[]), 
dbc.Row([   
        dbc.Col(       
            dcc.Graph(id="Mygraph_pressure"),
                ),
        ], align="center"),
],fluid = True) # para dar um respiro entre as bordas


@runSimulator.callback(Output('output-state', 'children'),
              Input("Run_simulator", 'n_clicks'),
              State("input_permeab", 'value'),
              State("input_skin_permab", 'value'),
              State("input_total_time", 'value'),
              State("input_flow_time", 'value'),
              State("input_porosity", 'value'),
              State("input_skin_radius", 'value'),
              State("input_flowrate", 'value'))
def update_output( n_clicks,input1, input2, input3, input4, input5, input6, input7):
    if n_clicks is None:
        # raise PreventUpdate
        return 'Off line'
    elif n_clicks == 1:
        #todo colocar aqui uma verificacao se os input nao sao NONE!!!!
        data_calculator=DataSourcereservoir()
        # input1=100
        # input2=50
        # input3=100
        # input4=10
        # input5=100
        # input6=10
        # input7=800
        data_calculator.get_variables(k_homo=input1,k_skin=input2,Phi=input3,r_skin=input4,total_time=input5,flow_time=input6,flow_rate=input7)
        data_calculator.caculate_data_using_reservoir()
        text='The simulatoin started'
        return text
        # text='The simulator will run with: K={}mD // Ks={}mD // Total time={}Days // Flow_time={}Days // Porosity={}  // Skin_radius={}m  // Flow_rate={}m3/day'.format(input1,input2,input3,input4,input5,input6,input7)
    else:        
        text='The simulatoin is running'

        return text


# def parse_contents(contents, filename, date):
#     content_type, content_string = contents.split(',')

#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             # Assume that the user uploaded a CSV file
#             df = pd.read_csv(
#                 io.StringIO(decoded.decode('utf-8')))
#             print(30*'#')
#             print(str(filename))
#             print(30*'#')
#         elif 'xls' in filename:
#             # Assume that the user uploaded an excel file
#             df = pd.read_excel(io.BytesIO(decoded))
#     except Exception as e:
#         print(e)
#         return html.Div([
#             'There was an error processing this file.'
#         ])

#     return html.Div([
#         html.H5(filename),
#         dash_table.DataTable(
#             data=df.to_dict('records'),
#             columns=[{'name': i, 'id': i} for i in df.columns],
#             page_size=15
#         ),
#         dcc.Store(id='stored-data', data=df.to_dict('records')),

#         html.Hr(),  # horizontal line

#         # For debugging, display the raw contents provided by the web browser
#         html.Div('Raw Content'),
#         html.Pre(contents[0:200] + '...', style={
#             'whiteSpace': 'pre-wrap',
#             'wordBreak': 'break-all'
#         })
#     ])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            print(30*'#')
            print(str(filename))
            print(30*'#')
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])
@runSimulator.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

def read_csv_return_df(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            print(30*'#')
            print(str(filename))
            print(30*'#')
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return df
@runSimulator.callback(Output('Mygraph_pressure', 'figure'), [
Input('upload-data', 'contents'),
Input('upload-data', 'filename')
])
def update_graph(contents, filename):
    x = []
    y = []
    if contents:
        contents = contents[0]
        filename = filename[0]
        df = read_csv_return_df(contents, filename)
        # df = df.set_index(df.columns[0])
        # print(30*'#')
        # print(df["Time[sec]"][:5])
        print(30*'@')
        x=df['Time[sec]']
        y=df['Pressure_sf[Pa]']
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x, 
                y=y, 
                mode='markers')
            ],)
    return fig

# @runSimulator.callback(Output('output-datatable', 'children'),
#               Input('upload-data', 'contents'),
#               State('upload-data', 'filename'),
#               State('upload-data', 'last_modified'))
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children


# @runSimulator.callback(Output('output-div', 'children'),
#               Input('upload_button','n_clicks'),
#               State('stored-data','data'),
#               State('xaxis-data','value'),
#               State('yaxis-data', 'value'))
# def make_graphs(n, data, x_data, y_data):
#     if n is None:
#         return dash.no_update
#     else:
#         bar_fig = px.bar(data, x=x_data, y=y_data)
#         # print(data)
#         return dcc.Graph(figure=bar_fig)





if __name__ == '__main__':
    runSimulator.run_server(debug=True, port=8000)