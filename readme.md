# Roadmap of Lagrange DAO

[![Made by LagrangeDAO](https://img.shields.io/badge/made%20by-LagrangeDAO-green.svg)](https://www.lagrangedao.com/)
[![Twitter Follow](https://img.shields.io/twitter/follow/lagrangedao)](https://twitter.com/lagrangedao)

![roadmap.svg](images%2Froadmap.svg)

## Installation

Clone the repository or download the code files.
Install the required packages:
```shell
pip install -r requirements.txt
```


Run the script:

    python roadmap_gantt.py

Note: The script generates a PNG image file of the chart in a new images directory. If the images directory does not exist, it will be created automatically.

## Usage

To customize the Gantt chart, edit the df list of task dictionaries in the script. Each dictionary represents a task and should have the following keys:

* Task (string): The name of the task.
* Start (string): The start date of the task in the format "YYYY-MM-DD".
* Finish (string): The finish date of the task in the format "YYYY-MM-DD".

To change the color scheme of the chart, edit the colors parameter in the create_gantt function call. The index_col and show_colorbar parameters can also be adjusted to change the appearance of the chart.

## License

This code is released under the MIT License. See LICENSE for details.

## Credits
This code was created  for Lagrange DAO.
