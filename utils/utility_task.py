import requests
import os
from config import BASE_URL_CARDS, HEADERS_ATT, QUERY, VAT_TASK_NAME, VAT_FILE_NAME

class Task:

    query = QUERY
    headers = HEADERS_ATT

    def __init__(self, api_id):
        self.api_id = api_id
        self.base_url = BASE_URL_CARDS + self.api_id + "/attachments"
        self.attachment_url = ""
        self.card_url = BASE_URL_CARDS + self.api_id


    def validate_task(self, name):
        self.name = name
        attachments = requests.get(self.base_url,headers=self.headers)
        if attachments.status_code == 200:
            count_attachment = len(attachments.json())
        else:
            return "bad response"

        if count_attachment==1:
            for attachment in attachments.json():
                self.attachment_url = attachment["url"]
                file_name = attachment["fileName"]
                ext = os.path.splitext(file_name)[1].lower()
                if name.lower().strip() == VAT_TASK_NAME.lower().strip():
                    if ext==".xlsx":
                        return "Valid"
                    else:
                        return "Not Valid"
                else:
                    return "Valid"
               
        else:
            return "Not Valid"



    def download_attachment(self):
        if self.attachment_url!="":
            response = requests.get(self.attachment_url,headers=self.headers)
            #file_name = self.attachment_url.split('/')[-1]

            if response.status_code == 200:
                with open(VAT_FILE_NAME, 'wb') as file:
                    file.write(response.content)
                    return VAT_FILE_NAME
            else:
                return (response.status_code + " - " + response.text)
        else:
            return ""

        

    def move_task(self, list_id):
        self.list_id = list_id
        body = {"idList": f"{list_id}"}
        response = requests.put(self.card_url, headers=self.headers, data=body)

    


