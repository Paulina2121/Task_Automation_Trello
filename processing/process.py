import csv
from scenarios.scenario_vat_checker import vat_checker
from config import TASK_LIST_FILE, ID_LIST_MANUAL, VAT_TASK_NAME
from utils.utility_task import Task
import sys

def run():
    row_to_add = []

    try:
        with open(TASK_LIST_FILE,"r") as file:
            reader = csv.DictReader(file,delimiter="|",fieldnames=["api_id","name","status"])
            for row in reader:
                process_task(row["api_id"] , row["name"], row["status"])
                row_to_add.append({"api_id":row["api_id"], "name":row["name"],"status":"processed"})
                    
        with open(TASK_LIST_FILE,"w",newline="\n") as file:
            writer = csv.DictWriter(file,delimiter="|",fieldnames=["api_id","name","status"])
            writer.writerows(row_to_add)

    except FileNotFoundError:
        sys.exit("File with task's list not found. Program exit")


def process_task(api_id, name, status):
    if status != "pending":
        return
    
    if name.strip().lower() == VAT_TASK_NAME.strip().lower():
        vat_checker(api_id)
    else:
        task = Task(api_id)
        task.move_task(ID_LIST_MANUAL)


if __name__ == "__run__":
    run()


