import pandas as pd
import sqlite3

print("Connecting to the data warehouse...")
conn = sqlite3.connect('football_warehouse.db')

sql_query = """
SELECT 
    t.TeamName,
    t.Country,
    p.Name AS PlayerName,
    p.Position,
    SUM(m.Goals_Scored) AS Total_Goals,
    SUM(m.Minutes_Played) AS Total_Minutes
FROM fact_matches m
JOIN dim_players p ON m.PlayerID = p.PlayerID
JOIN dim_teams t ON p.TeamID = t.TeamID
GROUP BY 
    t.TeamName, 
    t.Country, 
    p.Name, 
    p.Position
ORDER BY 
    Total_Goals DESC, 
    Total_Minutes DESC;
"""

print("Executing SQL JOIN query...")
final_dashboard_df = pd.read_sql_query(sql_query, conn)
final_dashboard_df.to_csv('final_dashboard_view.csv', index=False)
conn.close()

print("Full dashboard view generated with Player Names!")