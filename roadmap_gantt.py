import os
import plotly.express as px
import pandas as pd

import plotly.figure_factory as ff

df = pd.DataFrame([
    dict(Task="Milestone Setup", Start='2022-11-01', Finish='2022-12-31', Resource="MileStone 1"),
    dict(Task="Dataset", Start='2023-01-01', Finish='2023-03-01', Resource="MileStone 2"),
    dict(Task="Space", Start='2023-02-01', Finish='2023-04-01', Resource="MileStone 2"),
    dict(Task="Computing provider", Start='2023-03-01', Finish='2023-04-15', Resource="MileStone 3")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")

# fig.show()
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/roadmap.png")
fig.show()