import pandas as pd
import plotly_express as px

df = pd.read_csv('/Users/vivekkumar/Documents/python_projects/project-c103/data.csv')
fig = px.scatter(df, x = "date", y = "cases", color = "country", title = "")
fig.show()