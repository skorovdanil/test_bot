import requests
import json


webhook_url = 'https://h.albato.ru/h/7/qHSiSktVzqFIKjd2xHBslURmjpCddrZ0WhzYxQ%252B%252FAOE%253D'
headers = {
    'Content-Type': 'application/json'
}
data = {
    'key1': 'value1',
    'key2': 'value2'
}

response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

if response.status_code == 204:
    print('Webhook request sent successfully')
else:
    print('Failed to send webhook request. Status code:', response.status_code)

def ref(tel):
    response = requests.get('https://dev-bx.sskuban.ru/rest/2536/2t83d9x5ilqmlxp7/user.search.json?filter[PERSONAL_MOBILE]=89186366010&filter[ACTIVE]=true',verify=False)
    data = response.json()
    work_positions = ['Менеджер по продажам','Старший менеджер по продажам','Руководитель отдела продаж']
    if data["result"] != []:
        if data["result"][0]["WORK_POSITION"] in work_positions:
            #print("Вы менеджер")
            return True,data["result"][0]["ID"]
        else:
            return [False]
            #print("Вы не менеджер")
        #print(data["result"][0]["WORK_POSITION"])
    else:
        print("Неверный аккаунт")
        return [False]



from dotenv import load_dotenv
import os
load_dotenv()
BX_API = os.getenv("BX_API")
print(BX_API+"user.search.json")

#data = ref()
#if data[0] == True:
#    print(data[1])
#else:
#    print("Вы не менеджер")