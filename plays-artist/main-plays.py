import pandas as pd
import plotly.express as px

data = pd.read_csv("edited-data-plays.csv")
df = pd.DataFrame(data)
# fig = px.line(df, x="date", y='plays')
# fig.show()

fig = px.scatter(df, x="amount_of_songs", y="amount_of_plays", hover_data=["artist", "amount_of_songs", "amount_of_plays"])
fig.show()
