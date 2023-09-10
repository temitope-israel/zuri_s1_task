import datetime
from fastapi import FastAPI
import requests
from typing import Optional

app = FastAPI()


# Get Weekday
today = datetime.date.today()
weekday_name = today.strftime('%A')


# Get UTC Time
utc_time = datetime.datetime.today().replace(microsecond=0).isoformat()
final_utc_time = str(utc_time) + "Z"


# Get Status Response code
r = requests.get('https://google.com')
status_code = r.status_code



# Result 
personal_info = {
    "slack_name": "Omoniyi Temitope Israel",
    "current_day": weekday_name,
    "utc_time": final_utc_time,
    "track": "backend",
    "github_file_url": "https://github.com/temitope-israel/zuri_s1_task/blob/main/main.py",
    "github_repo_url": "https://github.com/temitope-israel/zuri_s1_task",
    "status_code" : status_code

}


@app.get("/api")
def api(slack_name, track):
    return personal_info