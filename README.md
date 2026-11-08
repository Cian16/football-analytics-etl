# End-to-End Football Analytics ETL Pipeline

**Live Dashboard:** [View on Tableau Public]([(https://public.tableau.com/app/profile/cian.buthello/viz/FootballAnalytics_17941188802980/Dashboard1))

## Project Overview
An automated Data Engineering pipeline that generates, extracts, transforms, and loads football match statistics into a local relational database for analytical querying and BI visualization. This project demonstrates core ETL principles, data cleaning, and relational database management.

## Architecture & Tech Stack
* **Data Generation & Extraction:** Python (`random`, `datetime`)
* **Transformation (Silver Layer):** Python (`pandas`) for handling null values, removing system duplicates, and correcting negative integer anomalies.
* **Data Warehouse (Gold Layer):** SQLite3 zero-configuration local database.
* **Analytics:** Complex SQL `JOIN` aggregations across Fact and Dimension tables.
* **Visualization:** Tableau Public for Business Intelligence reporting.

## Pipeline Workflow
1. **`generate_raw_data.py`**: Simulates unstructured, messy source data (CSVs) representing a 5-team league with 11-player 4-4-2 rosters. Introduces intentional data anomalies like missing positions and impossible goals.
2. **`etl_script.py`**: Extracts the raw CSVs, applies programmatic data cleaning protocols using Pandas, and loads the structured dataframes into `football_warehouse.db`.
3. **`sql_analysis.py`**: Connects directly to the SQLite database and executes analytical SQL queries to calculate total goals and minutes played by joining the `fact_matches`, `dim_players`, and `dim_teams` tables.

## Dashboard Insights
The final analytical view is exported and connected to a Tableau dashboard, featuring:
* A Golden Boot leaderboard highlighting top scorers.
* Club-level goal aggregations visualized through color-coded bar charts.
* Player efficiency scatter plots mapping Total Goals against Total Minutes.
* Validated positional metrics confirming data cleaning accuracy (Forwards averaging the highest output; Goalkeepers at zero).
