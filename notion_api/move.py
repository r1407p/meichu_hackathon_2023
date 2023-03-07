import requests,json
from notion.client import NotionClient
token =  "secret_8ItEG3yPsAGErF1arwCa2m5C70RD13GWWqLv1cuuvym"
database_id = "fe34c2bce09b4216b43e91825b94d6f4"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

response = requests.get(f"https://api.notion.com/v1/databases/{database_id}", headers=headers)

print(response.text)

def get_pages():
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    
    payload = {"page_size": 100}
    response  = requests.post(url,json=payload,headers=  headers)
    print(response)
    data = response.json()
    with open("db.json",'w',encoding="utf8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)
        
    results = data["results"]
    return results

print("hello world")

