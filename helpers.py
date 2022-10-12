import pandas as pd
import numpy as np

def who_win (team1, team2, df):
    team1_win = 0
    team2_win = 0
    for index, row in df.iterrows():
        if row['home_team'] == team1:
            if row['home_team_score'] > row['away_team_score']:
                team1_win += 1
            else:
                team2_win += 1
        else:
            if row['home_team_score'] > row['away_team_score']:
                team2_win += 1
            else:
                team1_win += 1

    print(team1 + " win " + str(team1_win) + " times")
    print(team2 + " win " + str(team2_win) + " times")

    if team1_win > team2_win:
        print("So, based on the historical matches, we predict that the winner is: " + team1)
        return "So, based on the historical matches, we predict that the winner is: " + team1
    elif team1_win < team2_win:
        print("So, based on the historical matches, we predict that the winner is: " + team2)
        return "So, based on the historical matches, we predict that the winner is: " + team2
    else:
        print("So, based on the historical matches, we predict that their winning rate is the same")
        return "So, based on the historical matches, we predict that their winning rate is the same"