import requests
import datetime
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# Get Weekday
today = datetime.date.today()
weekday_name = today.strftime('%A')


# Get UTC Time
utc_time = datetime.datetime.today()
utc_time = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')


# utc_time = datetime.datetime.today().replace(microsecond=0).isoformat()
# final_utc_time = str(utc_time) + "Z"
# utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')


# Get Status Response code
r = requests.get('https://apitask-1-c6145966.deta.app/api')
status_code = r.status_code



# Result 
personal_info = {
    "slack_name": "omoniyi_temitope",
    "current_day": weekday_name,
    "utc_time": utc_time,
    "track": "backend",
    "github_file_url": "https://github.com/temitope-israel/zuri_s1_task/blob/main/main.py",

    "github_repo_url": "https://github.com/temitope-israel/zuri_s1_task",
    "status_code" : status_code

}


@app.get("/api")
async def api(slack_name: str = "omoniyi_temitope", track: str = "backend"):
    return personal_info