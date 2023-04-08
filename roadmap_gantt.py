import os

import plotly.figure_factory as ff

df = [dict(Task="Milestone Setup", Start='2022-11-01', Finish='2022-12-31', Complete=100),
      dict(Task="Dataset", Start='2023-01-01', Finish='2023-03-01', Complete=80),
      dict(Task="Space", Start='2023-02-01', Finish='2023-04-01', Complete=60),
      dict(Task="Computing provider", Start='2023-03-01', Finish='2023-04-15', Complete=30)]

fig = ff.create_gantt(df, title="lagrange DAO Roadmap", colors='Viridis', index_col='Complete', show_colorbar=True)
# fig.show()
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/roadmap.png")
