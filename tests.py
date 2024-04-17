import requests

#url = "https://dev-bx.sskuban.ru/rest/3000/22439vfkmenns4n5/crm.lead.add.json"

data = {'FIELDS[TITLE]': 'Новый лид'}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('Лид успешно добавлен')
else:
    print('Ошибка при добавлении лида:', response.text)



    #dkngkdmfkdvmkl