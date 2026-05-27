import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/matches.csv")

# Create dashboard layout
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# -------------------------------
# 1. Top Winning Teams
# -------------------------------
wins = df['winner'].value_counts().head(5)

axes[0, 0].bar(wins.index, wins.values)

axes[0, 0].set_title("Top 5 Teams by Wins")
axes[0, 0].tick_params(axis='x', rotation=45)

# -------------------------------
# 2. Toss Decisions
# -------------------------------
toss = df['toss_decision'].value_counts()

axes[0, 1].pie(
    toss.values,
    labels=toss.index,
    autopct='%1.1f%%'
)

axes[0, 1].set_title("Toss Decisions")

# -------------------------------
# 3. Top Players of the Match
# -------------------------------
players = df['player_of_match'].value_counts().head(5)

axes[1, 0].bar(players.index, players.values)

axes[1, 0].set_title("Top Players of the Match")
axes[1, 0].tick_params(axis='x', rotation=45)

# -------------------------------
# 4. Matches Played Per Season
# -------------------------------
season_matches = df['season'].value_counts().sort_index()

axes[1, 1].plot(
    season_matches.index,
    season_matches.values,
    marker='o'
)

axes[1, 1].set_title("Matches Per Season")
axes[1, 1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Save dashboard
plt.savefig("charts/ipl_dashboard.png")

# Show dashboard
plt.show()

print("IPL Dashboard Created Successfully!")