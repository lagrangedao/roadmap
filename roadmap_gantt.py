import os
import plotly.express as px
import pandas as pd

import plotly.figure_factory as ff

df = pd.DataFrame([
    dict(Component="Milestone Setup", Start='2022-11-01', Finish='2022-12-31', Milestone="M1"),
    dict(Component="Dataset", Start='2023-01-01', Finish='2023-03-01', Milestone="M2"),
    dict(Component="Space", Start='2023-02-01', Finish='2023-04-01', Milestone="M2"),
    dict(Component="Computing provider", Start='2023-03-01', Finish='2023-04-15', Milestone="M3")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Component", color='Milestone')
fig.update_layout(
    font_family="Arial",
    title_font_family="Arial",
    title_font_color="black",
    legend_title_font_color="black"
)
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/roadmap.svg", engine='kaleido',width=800, height=400)
# fig.show()