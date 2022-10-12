#!/usr/bin/env python

#hello message
echo "Hello! Welcome to the World Cup Prediction Project!"
chmod +x query_sql.py
chmod +x querydb.py
chmod +x draw.py


echo "Please enter the object to sort:"
read object
./query_sql.py sort_df --object $object

echo "The frist team in the pair is:"
read team1
echo "The second team in the pair is:"
read team2
./query_sql.py who_would_win --team1 $team1 --team2 $team2

echo "Please enter the team to check group"
read team
./query_sql.py whichGroup --team1 $team

echo "Please enter the team to check historical games"
read team
./query_sql.py histGame --team1 $team

echo "Please enter the team to check players"
read team
./query_sql.py players --team1 $team

echo "Please enter the object to sort:"
read object
./query_sql.py drawpic --object $object

echo "Please enter the theme to draw:"
read theme
./query_sql.py drawpic --theme $theme
