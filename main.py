import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import datetime
from plotly.subplots import make_subplots

df = pd.read_csv("owid-covid-data.csv")
df = df.fillna(0)
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df.drop("date", axis=1, inplace=True)
df.to_csv("owid-covid-data.csv", index=False)
fig = px.scatter(df, x="year", y="total_deaths",color='continent')
fig.show()
df = df[['continent', 'year', 'total_deaths', 'new_deaths', 'diabetes_prevalence']]
print(df.corr())
# group the data by continent and year
df_grouped = df.groupby(['continent', 'year']).sum().reset_index()

# create a scatter plot to compare total deaths and deaths due to diabetes
fig = px.scatter(df_grouped, x="year", y="diabetes_prevalence", color="continent", size="new_deaths", hover_name="continent",template="plotly_dark",size_max=60,animation_frame="year",range_x=[2018,2025])
fig2 = px.scatter(df_grouped, x="total_deaths", y="diabetes_prevalence", color="continent", hover_data=['year'],size="new_deaths", hover_name="continent",template="plotly_dark",size_max=50)
fig.update_layout(title="Deaths due to Diabetes vs Total Deaths by Continent", xaxis_title="Year", yaxis_title="Deaths due to Diabetes",xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
fig2.update_layout(title="Deaths due to Diabetes vs Total Deaths by Continent", xaxis_title="Total Deaths", yaxis_title="Deaths due to Diabetes",xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
fig.show()
fig2.show()