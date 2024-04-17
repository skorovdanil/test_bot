import requests
import json
from dotenv import load_dotenv
import os
from db import users_db


load_dotenv()
BX_API = os.getenv("BX_API")


def ref(tel):
    work_positions = ['Менеджер по продажам', 'Старший менеджер по продажам', 'Руководитель отдела продаж']
    tel2 = tel.replace("8", "7", 1)
    tel3 = tel.replace("8", "+7", 1)
    tels = [tel, tel2, tel3]
    expected = False
    for telephone in tels:
        response_data = {
            "filter[PERSONAL_MOBILE]": [telephone],
            "filter[ACTIVE]": "true"
        }
        response = requests.get(BX_API+'user.search.json',params=response_data)
        data = response.json()
        if data["result"] != []:
            if data["result"][0]["WORK_POSITION"] in work_positions:
                # print("Вы менеджер")
                return True, data["result"][0]["ID"]
            else:
                return [False]
                # print("Вы не менеджер")
            # print(data["result"][0]["WORK_POSITION"])
    if not expected:
        return [False]

def is_active_ref(user_id):
    result_find = users_db.find_refer(user_id)
    is_active = False
    if result_find:
        response_data = {
            "filter[ID]": [result_find[0]]
        }
        response = requests.get(BX_API+'user.search.json',
                                params=response_data)
        data = response.json()
        if data['result'] != []:
            is_active = data['result'][0]['ACTIVE']
        return result_find[0], is_active
    else:
        return result_find, is_active

