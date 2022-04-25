from data_generation.simulator_01 import DataSourcereservoir



######################################################
# INSTANCIANDO O SIMULADOR PARA SER EXECUTADO
######################################################
data_calculator=DataSourcereservoir()

input1=100
input2=50
input3=100
input4=10
input5=100
input6=10
input7=800


data_calculator.get_variables(k_homo=input1,k_skin=input2,Phi=input3,r_skin=input4,total_time=input5,flow_time=input6,flow_rate=input7)
        # text='The simulator will run with: K={}mD // Ks={}mD // Total time={}Days // Flow_time={}Days // Porosity={}  // Skin_radius={}m  // Flow_rate={}m3/day'.format(input1,input2,input3,input4,input5,input6,input7)
data_calculator.caculate_data_using_reservoir()
text='The simulatoin is running'

print(text)