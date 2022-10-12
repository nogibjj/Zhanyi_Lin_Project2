
from fastapi import FastAPI
import databricks
from databricks import sql
from pyspark.sql.types import *
import os
from pyspark import SQLContext
import helpers
import pandas as pd
from googlesearch import search


def querydb(team1, team2):
    query="select date, tournament, home_team, away_team, home_team_score, away_team_score from default.historical_matches_csv where home_team = '%s' and away_team = '%s' or home_team = '%s' and away_team = '%s'" % (team1, team2,team2, team1)
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       =  os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
    if team1 == team2:
        print("The same team, please input two different teams")
        return "The same team, please input two different teams"
    elif team1 == "Portugal" or team2 == "Portugal":
        print("The winner is: Portugal because of Cristiano Ronaldo")
        return "The winner is: Portugal because of Cristiano Ronaldo"
    elif team1 == "France" or team2 == "France":
        print("The winner is: France because Benzema can be the new King of France")
        return "The winner is: France because Benzema can be the new King of France"
    else:
        df = pd.DataFrame(result)
        df.columns = ["date", "tournament", "home_team", "away_team", "home_team_score", "away_team_score"]
        #print(df)
        toReturn = helpers.who_win(team1, team2, df)
        return toReturn
def hisGame(team1):
    query="select date, tournament, home_team, away_team, home_team_score, away_team_score from default.historical_matches_csv where home_team = '%s' or away_team = '%s' " % (team1, team1)
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       =  os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
    #print(result)
    result = pd.DataFrame(result)
    result.columns = ["date", "tournament", "home_team", "away_team", "home_team_score", "away_team_score"]
    return result

def findPlayers(team1):
    
    query="select Team, Group, Player from default.fifa_world_cup_squads"
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       =  os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
    #print(result)
    df = pd.DataFrame(result)
    df.columns = ["Team", "Group", "Player"]
    #df = pd.read_csv("/workspaces/Zhanyi_Lin_Project1/2018 FIFA World Cup Squads.csv")
    #df.to_csv("/Users/a563186832/Desktop/Duke/2018_FIFA_World_Cup_Squads.csv")
    df = df[df["Team"] == team1]
    df = df[df.Team == team1]
    return df["Player"].tolist()

def findGroup(team1):
    
    query="select * from default.Qatar2022-teams"
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       =  os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result)

    #df = pd.read_csv("/workspaces/Zhanyi_Lin_Project1/Qatar2022-teams.csv")
    df2 = df.set_index("Team")
    group = df2["Group"].loc[team1]
    teams_in_same_team = df[df["Group"] == group].Team.tolist()
    teams_in_same_team.remove(team1)
    return "The teams in the same group are: " + ", ".join(teams_in_same_team) + ".They are in Group " + group + "."

def recentNews(team1):
    query = team1 + " world cup"
    toReturn = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        toReturn.append(j)
    return toReturn

def sorting(object):
    query="select date, tournament, home_team, away_team, home_team_score, away_team_score from default.historical_matches_csv" 
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       =  os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
    #print(result)
    result = pd.DataFrame(result)
    result.columns = ["date", "tournament", "home_team", "away_team", "home_team_score", "away_team_score"]
    result.sort_values(object)
    return result