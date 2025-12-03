# import_ANH_data.py

# Brief Description: This script import production and sales gas raw data from ANH website.

import pandas as pd

url = 'https://www.anh.gov.co/documents/28388/Producci%C3%B3n_Fiscalizada_Gas_2025_4yLgd5M.xlsx'

xls = pd.ExcelFile(url)
