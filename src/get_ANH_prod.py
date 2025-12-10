# import_ANH_data.py

# Brief Description: This script import production and sales gas raw data from ANH website.

import pandas as pd

url = 'https://www.anh.gov.co/documents/23123/Balance_producci%C3%B3n_de_Gas_2015.xlsx'

data = pd.read_excel(url, sheet_name = 'enero-15', skiprows = 6, skipfooter = 3)

xls = pd.ExcelFile(url)
hojas = xls.sheet_names