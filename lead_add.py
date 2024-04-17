import requests
import json
import manager_ref_bx
from dotenv import load_dotenv
import os

load_dotenv()
BX_API = os.getenv("BX_API")

def create_lead_bx24_buy_app(name,tel,message,reservation_data,user_id):
    tel1 = tel.replace(" ", "").replace("-", "")
    tel2 = tel1.replace("+7", "7")
    tel3 = tel1.replace("+7", "8")
    tel4 = tel1.replace("+7", "+8")
    tels = [tel1, tel2, tel3, tel4]
    expected = False
    find_refer = manager_ref_bx.is_active_ref(user_id)
    for telephone in tels:
        response_data = {
            "filter[PHONE]": [telephone],
            "filter[!STATUS_ID]": "CONVERTED"
        }
        response = requests.get(BX_API+'crm.lead.list.json',params=response_data)
        data = response.json()
        if data['result'] != []:
            #ПРОВЕРКА ЕСТЬ ЛИ РЕФЕРАЛ И АКТИВЕН ЛИ ОН
            #if find_refer and find_refer[1] == True:
            #    comment_data = {
            #        "fields[ENTITY_ID]": f"{data['result'][0]['ID']}",
            #        "fields[ENTITY_TYPE]": "lead",
            #        "fields[COMMENT]": f"<b>Новое сообщение от пользователя</b>\n"
            #                           f"ЖК {reservation_data['jk_name']}\n"
            #                           f"{reservation_data['rooms_name']}\n"
            #                           f"Литер {reservation_data['liter_num']}\n"
            #                           f"Подъезд {reservation_data['entrance']}\n"
            #                           f"№ кв {reservation_data['apartment_number']}\n"
            #                           f"Площадь {reservation_data['area_total']}\n"
            #                           f"Цена {reservation_data['price']}\n"
            #                           f"{message}"
            #    }
            #    response = requests.get(
            #        'https://bx.sskuban.ru/rest/3284/5mup6db3fzv3dm98/crm.timeline.comment.add.json',
            #        params=comment_data)
            #    expected = True
            #    return data
            #else:
            comment_data = {
                "fields[ENTITY_ID]": f"{data['result'][0]['ID']}",
                "fields[ENTITY_TYPE]": "lead",
                "fields[COMMENT]": f"<b>Новое сообщение от пользователя</b>\n"
                                   f"ЖК {reservation_data['jk_name']}\n"
                                   f"{reservation_data['rooms_name']}\n"
                                   f"Литер {reservation_data['liter_num']}\n"
                                   f"Подъезд {reservation_data['entrance']}\n"
                                   f"№ кв {reservation_data['apartment_number']}\n"
                                   f"Площадь {reservation_data['area_total']}\n"
                                   f"Цена {reservation_data['price']}\n"
                                   f"{message}"
            }
            response = requests.get(BX_API+'crm.timeline.comment.add.json',params=comment_data)
            expected = True
            return data
    if not expected:
        if find_refer[0] is not None and find_refer[1] == True:
            lead_data = {
                "fields[TITLE]": f"{name} - telegram - {tel}",
                "fields[NAME]": name,
                "fields[PHONE][0][VALUE]": tel1,
                "fields[PHONE][0][VALUE_TYPE]": "WORK",
                "fields[SOURCE_ID]": "UC_QWI3AK",
                "fields[SOURCE_DESCRIPTION]": "Реферал",
                "fields[ASSIGNED_BY_ID]":f"{find_refer[0]}",
                "fields[COMMENTS]": f"ЖК {reservation_data['jk_name']}\n"
                                    f"{reservation_data['rooms_name']}\n"
                                    f"Литер {reservation_data['liter_num']}\n"
                                    f"Подъезд {reservation_data['entrance']}\n"
                                    f"№ кв {reservation_data['apartment_number']}\n"
                                    f"Площадь {reservation_data['area_total']}\n"
                                    f"Цена {reservation_data['price']}\n"
                                    f"{message}"
            }
        else:
            lead_data = {
                "fields[TITLE]": f"{name} - telegram - {tel}",
                "fields[NAME]": name,
                "fields[PHONE][0][VALUE]": tel1,
                "fields[PHONE][0][VALUE_TYPE]": "WORK",
                "fields[SOURCE_ID]": "UC_QWI3AK",
                "fields[SOURCE_DESCRIPTION]": reservation_data['liter_address'],
                "fields[COMMENTS]": f"ЖК {reservation_data['jk_name']}\n"
                                   f"{reservation_data['rooms_name']}\n"
                                   f"Литер {reservation_data['liter_num']}\n"
                                   f"Подъезд {reservation_data['entrance']}\n"
                                   f"№ кв {reservation_data['apartment_number']}\n"
                                   f"Площадь {reservation_data['area_total']}\n"
                                   f"Цена {reservation_data['price']}\n"
                                   f"{message}"
            }
        response = requests.get(BX_API+'crm.lead.add.json',params=lead_data)
        return("Такого номера нет")


def create_lead_bx24_chat_app(name,tel,message,user_id, support_country):
    tel1 = tel.replace(" ", "").replace("-", "")
    tel2 = tel1.replace("+7", "7")
    tel3 = tel1.replace("+7", "8")
    tel4 = tel1.replace("+7", "+8")
    tels = [tel1, tel2, tel3, tel4]
    expected = False
    find_refer = manager_ref_bx.is_active_ref(user_id)
    for telephone in tels:
        response_data = {
            "filter[PHONE]": [telephone],
            "filter[!STATUS_ID]": "CONVERTED"
        }
        response = requests.get(BX_API+'crm.lead.list.json',params=response_data)
        data = response.json()
        if data['result'] != []:
            comment_data = {
                "fields[ENTITY_ID]": f"{data['result'][0]['ID']}",
                "fields[ENTITY_TYPE]": "lead",
                "fields[COMMENT]": f"<b>Новое сообщение от пользователя</b>\n"

            }
            response = requests.get(BX_API+'crm.timeline.comment.add.json',params=comment_data)
            expected = True
            return data
    if not expected:
        if find_refer[0] is not None and find_refer[1] == True:
            lead_data = {
                "fields[TITLE]": f"{name} - telegram - {tel}",
                "fields[NAME]": name,
                "fields[PHONE][0][VALUE]": tel1,
                "fields[PHONE][0][VALUE_TYPE]": "WORK",
                "fields[SOURCE_ID]": "UC_QWI3AK",
                "fields[ASSIGNED_BY_ID]": f"{find_refer[0]}",
                "fields[COMMENTS]": f"{message}"
            }
        else:
            lead_data = {
                "fields[TITLE]": f"{name} - telegram - {tel}",
                "fields[NAME]": name,
                "fields[PHONE][0][VALUE]": tel1,
                "fields[PHONE][0][VALUE_TYPE]": "WORK",
                "fields[SOURCE_ID]": "UC_QWI3AK",
                "fields[SOURCE_DESCRIPTION]": support_country,
                "fields[COMMENTS]": f"{message}"
            }
        response = requests.get(BX_API+'crm.lead.add.json',params=lead_data)
        return("Такого номера нет")

#name = "Даниил"
#tel = "+7 962 854-65-90"
#print(create_lead_bx24(name,tel))