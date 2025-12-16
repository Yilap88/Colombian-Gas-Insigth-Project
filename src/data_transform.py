# ANH_data_transform.py

# This scripts transform ANH raw data into a clean format by year for analysis. Hola mundo

## Imports packages
import numpy as np
import pandas as pd
import os


## Change working directory(/Colombian-Gas-Insight-Project/)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")


## Define input directory and initialize dictionaries
excel_files = os.listdir('Data/raw_data/ANH_gas_prod/') # create a list with all excel files names in the directory
datayear_dic = {} # create an empty dictionary to store excel per year dataframes
sheet_dict = {} # create an empty dictionary to store excel sheet dataframes
namelist = ['AÑO', 'MES', 'CAMPO', 'CONTRATO', 'EMPRESA', 'DEPARTAMENTO',
       'MUNICIPIO', 'PRODUCCION_FISCALIZADA', 'GASLIFT', 'GAS_REINYECTADO',
       'GAS_QUEMADO', 'CONSUMO_EN_CAMPO', 'ENVIADO_A_PLANTA', 'GAS_TRANSFORMADO',
       'ENTREGADO_A_GASEODUCTOS']

## Process each excel file and its sheets
for excel in excel_files: # loop through each excel file in the directory
    data_dir = f'Data/raw_data/ANH_gas_prod/{excel}' # create the path for each excel file
    sheet_names = pd.ExcelFile(data_dir).sheet_names[1:] # create a list with all sheet names except the first one


    for sheet in sheet_names: # loop through each sheet in the excel file
        tempdf = pd.read_excel(data_dir, sheet_name=sheet, skiprows=6, skipfooter=3) # read each sheet into a dataframe and store it in the sheet_dict
        tempdf.columns =  namelist # assign the predefined column names to the dataframe
        sheet_dict[sheet] = tempdf

    datayear_dic[excel] = pd.concat(sheet_dict.values()) # concatenate all sheets dataframes into a single dataframe per excel file and store it in the datayear_dic

final_df = pd.concat(datayear_dic.values()) # concatenate all excel dataframes into a single final dataframe


final_df.to_csv('Data/processed_data/ANH_gas_concat.csv', index=False) # save the final dataframe to an csv file
#final_df.to_excel('Data/processed_data/ANH_gas_concat.xlsx', index=False) # save the final dataframe to an excel file
