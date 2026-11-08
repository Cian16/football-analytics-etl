import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Generate Teams Data 
teams = pd.DataFrame({
    'TeamID': [10, 11, 12, 13, 14],
    'TeamName': ['Manchester City', 'Real Madrid', 'AEK Athens', 'Bayern Munich', 'Inter Milan'],
    'Country': ['England', 'Spain', 'Greece', 'Germany', 'Italy']
})
teams.to_csv('raw_teams.csv', index=False)

# 2. Generate Balanced Players Data (11 players per team - 4-4-2 formation)
roster_template = ['Forward', 'Forward', 'Midfielder', 'Midfielder', 'Midfielder', 'Midfielder', 'Defender', 'Defender', 'Defender', 'Defender', 'Goalkeeper']
player_data = []
player_id = 100

for team_id in [10, 11, 12, 13, 14]:
    for pos in roster_template:
        player_data.append({
            'PlayerID': player_id,
            'Name': f'Player_{player_id}',
            'TeamID': team_id,
            'Position': pos,
            'Weekly_Wage': random.randint(5000, 200000)
        })
        player_id += 1

players = pd.DataFrame(player_data)

# Intentionally break a couple of positions to null so our ETL script still has something to clean
players.loc[14, 'Position'] = None
players.loc[32, 'Position'] = None

players.to_csv('raw_players.csv', index=False)

# 3. Generate Smart Match Stats (Updated to include all 55 players)
match_data = []
for _ in range(500):
    pid = random.randint(100, 154) # Range updated to cover 5 teams * 11 players
    
    pos_value = players[players['PlayerID'] == pid]['Position'].values[0]
    pos = pos_value if pd.notna(pos_value) else 'Unknown'
    
    if pos == 'Forward':
        goals = random.choice([0, 0, 1, 2, 3, -1])
    elif pos == 'Midfielder':
        goals = random.choice([0, 0, 0, 1, 2, -1])
    elif pos == 'Defender':
        goals = random.choice([0, 0, 0, 0, 0, 1, -1])
    else: 
        goals = random.choice([0, 0, 0, -1]) 
        
    match_data.append({
        'MatchID': random.randint(1000, 1500),
        'PlayerID': pid,
        'Match_Date': (datetime(2025, 8, 1) + timedelta(days=random.randint(0, 250))).strftime('%Y-%m-%d'),
        'Goals_Scored': goals,
        'Minutes_Played': random.randint(-15, 90)
    })
    
matches = pd.DataFrame(match_data)
matches = pd.concat([matches, matches.sample(15)], ignore_index=True)
matches.to_csv('raw_match_stats.csv', index=False)
print("Balanced football dataset (11-man rosters) generated successfully!")