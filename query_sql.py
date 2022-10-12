#!/usr/bin/env python
from cmd import PROMPT
import click
from requests import head
import querydb
import pandas as pd
import spark
import helpers
import draw
import streamlit as st
# build  click commands for query directly
# build a click group
@click.group()
def cli():
#    """A simple CLI to query a SQL database"""
    "do something"


# build  click commands for query directly
@cli.command("who_would_win")
@click.option('--team1', default="Portugal", help='Number of greetings.')
@click.option('--team2', default="Brazil", help='Number of greetings.')
def cli_query(team1, team2):
    """Input two teams for historical matches"""
    querydb.querydb(team1, team2)


@cli.command("histGame")
@click.option('--team1', default="Portugal", help='Number of greetings.')
def hisGame(team1):
    """input a team to get its historical matches"""
    print(querydb.hisGame(team1))

@cli.command("players")
@click.option('--team1', default="Portugal", help='Which team you want to check.')
def players(team1):
    """Input a team for players"""
    print(querydb.findPlayers(team1))

@cli.command("whichGroup")
@click.option('--team1', default="Portugal", help='Number of greetings.')
def whichGroup(team1):
    """input a team to find which group it is"""
    print(querydb.findGroup(team1))

@cli.command("recent")
@click.option('--team1', default="Portugal", help='See the recent news of a team')
def recent(team1):
    """input a team to see the recent news"""
    links = querydb.recentNews(team1)
    for l in links:
        st.write("check out this [link]({a})".format(a=l))
        
@cli.command("drawpic")
@click.option('--theme', default="pandas play soccer", help='Who you want to draw')
def drawpic(theme):
    """input a theme to draw a picture"""
    print("drawing the picture of " + theme)
    draw.draw_pic(theme)
    
@cli.command("sort_df")
@click.option('--object', default="home_team", help='Who you want to draw')
def sort_df(object):
    """input a theme to draw a picture"""
    querydb.sorting(object)

# run the CLI
if __name__ == "__main__":
    cli()