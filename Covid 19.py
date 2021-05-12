import pandas as pd
import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.line(df , x = "cases" , y = "country" , color = "date")
fig.show()
