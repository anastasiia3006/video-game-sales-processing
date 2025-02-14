# video game sales processing

 Video Game Sales Analysis

This project analyzes video game sales data to determine:
    The most popular genres.
    The years with the highest sales.
    Whether specific consoles specialize in certain genres.

 Files
    vgchartz-2024.csv → Raw video game sales data.
    filled_data_vgchartz.csv → Processed dataset with missing values filled.
    main.py → Processes the raw dataset (cleans, fills missing data, saves to CSV).
    analyse_data.py → Performs analysis & visualization (popular genres, best-selling years, console preferences).
    problems to table.txt → Summary of findings.

 Analysis & Insights

 Most Popular Genres
    Shooter
    Action
    Misc

 Best Year for Sales → 2009 had the highest sales.

 Console Specialization
    PC → Most games (1069)
    DS → Second most (825)
    Android (And) → Third (677)

 Visualizations
    Most Popular Genres
    Top 5 Genres Over Time
    Most Popular Genre per Console

 How to Use
    Install dependencies:

    pip install pandas matplotlib seaborn

Run main.py to process data.
Run analyse_data.py to generate insights.
