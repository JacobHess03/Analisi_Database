Video Game Sales Analysis

This Python project allows you to analyze a video game dataset (in CSV format) through an interactive terminal menu. The analyses include sales by region, year, platform, genre, publisher, and more.
Requirements

    Python 3.7 or higher
    Python modules:
        csv
        numpy

Dataset

The program requires a file named videogame.csv in the same directory as the script. The file must contain the following columns:

    Name
    Platform
    Year
    Genre
    Publisher
    NA_Sales
    EU_Sales
    JP_Sales
    Other_Sales
    Global_Sales

Execution

To start the program, run:
Bash

    python nome_file.py

Features

From the interactive menu, you can select one of the following options:

    Total Sales by Region
    Calculates total sales for a specified region: NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales.

    Game Sales by Year
    By entering the game name and year, it shows global sales for that year.

    Platform with Most Global Sales
    Determines the platform with the highest total sales.

    Publisher with Most Global Sales

    Best-Selling Genre Globally

    Average Sales by Genre

    Annual Sales Trend by Platform
    Displays the sum of sales per year for a selected platform.

    Minimum Annual Sales by Publisher
    Shows the lowest recorded sales each year for a specific publisher.

    Top 10 Games by Global Sales

    Exit Program

Notes

    CSV rows with missing or erroneous data will be automatically ignored.
    The program is compatible with Python 3.10+ for the use of the match-case construct.

Authors: Giacomo Visciotti, Giovanni Pisaniello
