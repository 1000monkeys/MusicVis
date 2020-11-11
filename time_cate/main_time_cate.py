import pandas as pd
import plotly.express as px

data = pd.read_csv("edited-data-time-cat.csv", header=None)
df = pd.DataFrame(data)
# fig = px.line(df, x="date", y='plays')
# fig.show()

print(df)

fig = px.imshow(df,
                labels=dict(x="Day of Week", y="Time of Day", color="Amount of plays"),
                x=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                y=["Morning", "Afternoon", "Evening"]
                )
fig.show()
