import pandas as pd
import plotly.express as px

dataset = pd.read_excel("./data/BD_HackMTY_ChoquesYSiniestrosMONTERREY_2020_V2.xlsx")
postal_df = dataset['CODIGO POSTAL'].value_counts()[:9]
most_common_pc=list(postal_df.index)
df_map1 = dataset[['LONG','LAT','CODIGO POSTAL']]
df_map1.dropna(axis=0, inplace=True)
df_map1 = df_map1[df_map1['CODIGO POSTAL'].isin(most_common_pc)]

px.set_mapbox_access_token('pk.eyJ1IjoicmFtb25wdW9uIiwiYSI6ImNreW9vM3kydjAyMGoycG55ZmZsenI2bDEifQ.xreL88Eh1Zj3G2R_gwSlkA')
fig = px.scatter_mapbox(df_map1, lat= 'LAT', lon='LONG', color = 'CODIGO POSTAL', color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=9.5)
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=True) 