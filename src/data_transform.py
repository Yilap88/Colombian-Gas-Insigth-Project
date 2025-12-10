# ANH_data_transform.py

## This scripts transform ANH raw data into a clean format by year for analysis.

## Imports packages
import pandas as pd
import os

# def transform_ANH_data(location):
    # Drop rows with all NaN values
#    df_cleaned = df.dropna(how='all')
    
#    return df_filtered

# Working directory setting (/Colombian-Gas-Insight-Project/)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")


data_loc = 'Data/raw_data/ANH_gas_prod/Produccion_Fiscalizada_Gas_2013.xlsx'

data = pd.read_excel(data_loc, sheet_name='enero-13', skiprows=9, skipfooter=3)

data.head()



