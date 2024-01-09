# Spotify CLI Dashboard

![Dashboard Image](/dashboard.png)

## Overview
This project features a command-line interface (CLI) dashboard designed to display some insights extracted from a Spotify dataframe. The process involves cleaning the dataframe using PySpark, as demonstrated in the Jupyter notebook. The filtered dataframe is then utilized to visualize compelling information through the dashboard.

The dashboard is implemented in Python and leverages the "rich" library, enabling the creation and styling of layouts and texts within the terminal. Additionally, graph plotting libraries are employed to enhance the visualization of data.

## Process
1. **Data Cleaning:** The initial step involves cleaning the Spotify dataframe using PySpark. Refer to the accompanying Jupyter notebook for a detailed walkthrough of the cleaning process.

2. **Dashboard Creation:** The core of the project is a CLI dashboard designed in Python. The "rich" library is utilized to craft visually appealing layouts and texts within the terminal. This includes the incorporation of graph plotting libraries to present insightful visualizations.

## How to Run
To execute the project, follow these steps:

1. **Install Dependencies:** Make sure to install the required dependencies by running:
    ```
    pip install rich pyspark
    ```

2. **Run the Jupyter Notebook:** Execute the Jupyter notebook to perform data cleaning on the Spotify dataframe.

3. **Run the CLI Dashboard:** Run the Python script responsible for generating the CLI dashboard. Ensure that the necessary libraries and dependencies are installed.
   ```bash
   python app.py
