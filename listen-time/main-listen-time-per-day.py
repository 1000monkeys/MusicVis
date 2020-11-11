import pandas as pd
import plotly.express as px

data = pd.read_csv("data-edited-listen-time-per-day.csv")
df = pd.DataFrame(data)
# fig = px.line(df, x="date", y='plays')
# fig.show()

fig = px.area(df, x="date", y="plays")
fig.show()