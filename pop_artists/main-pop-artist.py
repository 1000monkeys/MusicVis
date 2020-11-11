import pandas as pd
import plotly.express as px

data = pd.read_csv("edited-data-pop-artist.csv")
df = pd.DataFrame(data)
# fig = px.line(df, x="date", y='plays')
# fig.show()

fig = px.bar(df, x="artist", y="amount_of_plays", hover_data=["artist", "amount_of_plays"])
fig.show()
