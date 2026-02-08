from utils.utility_task import Task
import pandas as pd
from web_scrapper.web_scraper import scraper
from config import ID_LIST_DONE, ID_LIST_EXC, VAT_TASK_NAME, MAX_RETRIES
import exceptions


def vat_checker(task_id):
    task = Task(task_id)
    is_valid = task.validate_task(VAT_TASK_NAME.strip().lower())
    

    if not is_valid:
        print("task: " + task_id +": attachment error")
        task.move_task(ID_LIST_EXC)
        return

    file_name = task.download_attachment()

    if not (file_name != "" or file_name.find(".xls")>0):
        print("task: " + task_id +": attachment error")
        task.move_task(ID_LIST_EXC)
        return

    df = pd.read_excel(file_name)

    df["Name"] = df["Name"].astype("string")
    df["Address"] = df["Address"].astype("string")
    df["Valid"] = df["Valid"].astype("string")

    try:    
        for index, row in df.iterrows():
            try:
                vat_number = row["VAT number"].strip()
                country = vat_number[:2]
                vat_id = vat_number[-(len(vat_number)-2):]
            except KeyError:
                raise exceptions.BusinessException("Missing column in the VAT file")

            result = get_row_data(vat_id, country)
            df.at[index,"Name"]=result["name"]
            df.at[index,"Address"]=result["address"]
            df.at[index,"Valid"]=result["result"]


        df.to_excel(file_name, index=False)
        task.move_task(ID_LIST_DONE)
            
    except exceptions.BusinessException as e:
        print("Error: task: " + task_id + " " + str(e))
        task.move_task(ID_LIST_EXC)
    except Exception as e:
        print("Unexpected Error: task: " + task_id + " " + str(e))
        task.move_task(ID_LIST_EXC)
  


def get_row_data(vat_id, country):
    for _ in range(MAX_RETRIES):
        try:
            result = scraper(vat_id, country)
            break
        except exceptions.BusinessException as e:
            result = {"name":"scrapping error","address":"scrapping error","result":"scrapping error" + str(e)}
            break
        except Exception as e:
            result = {"name":"scrapping error","address":"scrapping error","result":"scrapping error" + str(e)}
            continue

    return result



if __name__ == "__vat_checker__":
    vat_checker()
