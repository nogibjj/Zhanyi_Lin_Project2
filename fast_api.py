from fastapi import FastAPI
import uvicorn
import querydb
import query_sql
import spark
import helpers

app = FastAPI()


@app.get("/")
async def root():
    
    #return {"result": querydb.querydb(team1, team2)}
    return {"message": "Give more information to get the result. You can choose from any two teams who are going to participate World Cup 2022. You may reference https://www.fifa.com/fifaplus/en/articles/qatar-2022-all-qualified-teams-groups-dates-match-schedule-tickets-more for more information."}

@app.get("/{team1}/{team2}")
async def test_query(team1, team2):
    
    return {"result": querydb.querydb(team1, team2)}
    #return {"result": querydb.querydb()}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0")
