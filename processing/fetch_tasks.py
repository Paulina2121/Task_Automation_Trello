import requests
import csv
import sys
from config import URL_FETCH_TASKS, HEADERS, QUERY, TASK_LIST_FILE

def fetch_tasks():
  url = URL_FETCH_TASKS

  response = requests.request(
    "GET",
    url,
    headers=HEADERS,
    params=QUERY
  )


  try:
    if response.status_code != 200:
      response.raise_for_status()

    try:
      results = response.json()
    except ValueError:
       sys.exit("Response is not valid JSON")

    if not results:
       print("Empty response body - no new tasks to collect.")
       return


    rows_to_add = []
    for result in results:
        rows_to_add.append({"api_id":result["id"], "name":result["name"],"status":"pending"})

    with open(TASK_LIST_FILE,"w",newline="\n") as file:
        writer = csv.DictWriter(file,delimiter="|",fieldnames=["api_id","name","status"])
        writer.writerows(rows_to_add)

  except requests.exceptions.HTTPError:
     sys.exit("API error: Unable to retrieve tasks from Trello")



if __name__ == "__fetch_tasks__":
    fetch_tasks()