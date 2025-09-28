# Gas Data Downloading

# This data comes from the API of [gov.co](https://www.datos.gov.co/Minas-y-Energ-a/Gr-fico-Producciones-de-Gas-ANH/ppru-7duu), "gov.co" provides open data on matters relating to Colombian, including  the "ANH Colombian Gas Production"

# This script makes a time interactive gas production map, using department filter.



#!/usr/bin/env python

# make sure to install these packages before running:
#pip install pandas
#pip install sodapy
#pip install plotly
#pip install geopandas

# IMPORT LIBRARIES
import pandas as pd
import plotly as plotly
from sodapy import Socrata
import os
import geopandas as gpd


# SET THE WORKING DIRECTORIES
currentdir = os.path.abspath(__file__)
par_dir = os.path.dirname(currentdir)
new_dir = os.path.dirname(par_dir)
os.chdir(new_dir)


# UPLOAD THE PRODUCTION DATA
dfslider = pd.read_csv("Data/dfsliderdata.csv")


# UPLOAD THE MAP DATA
map = gpd.read_file("Data/MapsSF/MGN2022_DPTO_POLITICO/MGN_DPTO_POLITICO.shp")
print(map.head())
mapgeojson = map.to_json()
map.to_file("Data/MapsSF/departamentos.geojson", driver="GeoJSON")

# CREATE THE MAP
import plotly.express as px

fig = px.choropleth(
    dfslider,
    geojson=mapgeojson,
    featureidkey="properties.DPTO_CCDGO",  # ajusta según tu shapefile
    locations="coddanedepartamento",
    color="produccionkpc",
    color_continuous_scale="YlOrRd",
    title="Producción de Gas por Departamento"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()

