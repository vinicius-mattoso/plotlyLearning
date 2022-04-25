# Loading the modules
import numpy as np
import pandas as pd 

class DataSourcereservoir(object):

    def __init__(self,k_homo=None,k_skin=None,Phi=None,r_skin=None,total_time=None,flow_time=None,flow_rate=None):
        self.k_homo=k_homo
        self.k_skin=k_skin
        self.Phi=Phi
        self.r_skin=r_skin
        self.flow_rate=flow_rate
        self.flow_time=flow_time
        self.total_time=total_time


    def get_variables(self,k_homo=None,k_skin=None,Phi=None,r_skin=None,total_time=None,flow_time=None,flow_rate=None):
        self.k_homo=k_homo
        self.k_skin=k_skin
        self.Phi=Phi
        self.r_skin=r_skin
        self.flow_rate=flow_rate
        self.flow_time=flow_time
        self.total_time=total_time

    def caculate_data_using_reservoir(self):

        #####################################################################################
        # VOU CRIAR UMAS FUNCOES ALEATORIAS QUE VAO SUBSTITUIR O SIMULADOR DE RESERVATORIOS #
        #####################################################################################

        Time_plot=np.linspace(start=0,stop=self.total_time,num=1000)
        vazao=[]
        p_sandface=[]
        T_sandface=[]
        for i in np.arange(0,len(Time_plot)):
            aux=self.flow_rate+np.random.random()*5/100*self.flow_rate
            vazao.append(aux)
            aux_press=10*(aux**2)-5*(aux)+1
            aux_temp=-5*(aux**2)+10*(aux)+10
            p_sandface.append(aux_press)
            T_sandface.append(aux_temp)

        # converting list to array
        p_sandface = np.array(p_sandface)
        T_sandface = np.array(T_sandface)

        data={'Time[sec]':Time_plot,'Pressure_sf[Pa]':p_sandface,'Temperature_sf[K]':T_sandface}
        
        # Calling DataFrame constructor  
        df_results = pd.DataFrame(data)


        # df.to_csv (r'C:\Users\John\Desktop\export_dataframe.csv', index = None, header=True) 
        # path='r'D:\VINICIUS_DESKTOP\WellTestingAPI\results''
        file_name='Teste_numero_03'   
        base='./results/'
        location=base
        file = location + file_name + '.csv'
        # file = file_name + '.csv'
        df_results.to_csv(file,index=False)
        print('!!SIMULACAO FOI EXECUTADA COM SUCESSO!!')
