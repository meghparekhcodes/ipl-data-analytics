import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("🏏 IPL Data Analytics Dashboard")

# Load dataset
df = pd.read_csv("data/matches.csv")

# Show raw data
if st.checkbox("Show Dataset"):
    st.write(df.head())

# -------------------------------
# Top Teams
# -------------------------------
st.subheader("Top 5 IPL Teams by Wins")

wins = df['winner'].value_counts().head(5)

fig1, ax1 = plt.subplots()

ax1.bar(wins.index, wins.values)

plt.xticks(rotation=45)

st.pyplot(fig1)

# -------------------------------
# Toss Decisions
# -------------------------------
st.subheader("Toss Decisions")

toss = df['toss_decision'].value_counts()

fig2, ax2 = plt.subplots()

ax2.pie(
    toss.values,
    labels=toss.index,
    autopct='%1.1f%%'
)

st.pyplot(fig2)

# -------------------------------
# Top Players
# -------------------------------
st.subheader("Top Player of the Match Winners")

players = df['player_of_match'].value_counts().head(5)

fig3, ax3 = plt.subplots()

ax3.bar(players.index, players.values)

plt.xticks(rotation=45)

st.pyplot(fig3)