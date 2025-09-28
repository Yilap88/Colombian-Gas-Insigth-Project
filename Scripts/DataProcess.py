# Gas Data Downloading

# This data comes from the API of [gov.co](https://www.datos.gov.co/Minas-y-Energ-a/Gr-fico-Producciones-de-Gas-ANH/ppru-7duu), "gov.co" provides open data on matters relating to Colombian, including  the "ANH Colombian Gas Production"

# This script makes a ETL process, Extract the data from the API, transform the data and saved the data in the repository.

#!/usr/bin/env python

# make sure to install these packages before running:
#pip install pandas
#pip install sodapy
#pip install plotly
#pip install geopandas


import pandas as pd
from sodapy import Socrata
import os

# SOCRATA / API DATA DOWNLOAD
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("www.datos.gov.co", None)
# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")
# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("5dux-bfvx", limit=200000)
# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

# SET THE WORKING DIRECTORIES

currentdir = os.path.abspath(__file__)
par_dir = os.path.dirname(currentdir)
new_dir = os.path.dirname(par_dir)
os.chdir(new_dir)


# Create the database for the time slider production map and save it

dfslider = df[["vigencia", "mes", "coddanedepartamento", "departamento", "produccionkpc"]]
dfslider.to_csv("Data/dfsliderdata.csv", index=False)


df = dfslider[dfslider["vigencia"] == "2024"]
df_grouped = df.groupby("departamento")["produccionkpc"].sum()
df_grouped.to_csv("Data/dfsliderdata.csv", index=False)


print(df_grouped)


#df_grouped = df.groupby(["departamento", "vigencia"])["produccionkpc"].sum()
#print(df_grouped)
