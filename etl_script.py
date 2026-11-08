import pandas as pd
import sqlite3

print("Starting ETL Pipeline...")

# --- 1. EXTRACT ---
print("Extracting raw CSV data...")
teams_df = pd.read_csv('raw_teams.csv')
players_df = pd.read_csv('raw_players.csv')
matches_df = pd.read_csv('raw_match_stats.csv')

# --- 2. TRANSFORM ---
print("Cleaning data...")
# A. Fill missing positions with 'Unknown'
players_df['Position'] = players_df['Position'].fillna('Unknown')

# B. Remove duplicate match records (simulating system extraction glitches)
matches_df = matches_df.drop_duplicates()

# C. Fix negative minutes (convert to absolute value)
matches_df['Minutes_Played'] = matches_df['Minutes_Played'].abs()

# D. Fix negative goals (data entry errors, replace with 0)
matches_df.loc[matches_df['Goals_Scored'] < 0, 'Goals_Scored'] = 0

# --- 3. LOAD ---
print("Loading clean data into SQLite database...")
# This automatically creates the database file if it doesn't exist
conn = sqlite3.connect('football_warehouse.db')

# Push dataframes into SQL tables
teams_df.to_sql('dim_teams', conn, if_exists='replace', index=False)
players_df.to_sql('dim_players', conn, if_exists='replace', index=False)
matches_df.to_sql('fact_matches', conn, if_exists='replace', index=False)

conn.close()
print("Step 2 Complete: Clean data loaded into 'football_warehouse.db'.")