from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove , WebAppInfo , WebAppData
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
import json

#def read_data():
#    while True:
#        with open('json/data.json', 'r', encoding='utf-8') as file:
#            encode_data = json.load(file)
#        info_block = json.loads(encode_data)
#        return info_block
with open('json/data.json','r', encoding='utf-8') as file:
    data = json.load(file)

decode_data = json.loads(data)

CountinueMenu = [
  [KeyboardButton(text="⬅ Главное меню")]
]
CountinueMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=CountinueMenu)

MainMenuButton = KeyboardButton(text="⬅ Главное меню")

BackMenu = [
    [KeyboardButton(text="⬅ Назад"),
    KeyboardButton(text="⬅ Главное меню")]
]
BackMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=BackMenu)

BackMenuButton = KeyboardButton(text="⬅ Назад")


krasnodar_jk = ['Сегодня','Дом на Луговой','Дом на Московской','Ракурс','Жилой квартал Лучший','Дыхание','Свобода','Сердце','Фонтаны','Открытие']
kaliningrad_jk = ['Включи']
anapa_jk = ['Песчаный','Аванта']
maikop_jk = ['Дружба']
all_jk = ['Сегодня','Дом на Луговой','Дом на Московской','Ракурс','Жилой квартал Лучший','Дыхание','Свобода','Сердце','Фонтаны','Включи','Дружба' ,'Песчаный','Аванта','Открытие']
city = ['Краснодар','Анапа','Калининград','Майкоп']


# Main menu

MainMenu = [
    [KeyboardButton(text="🏢 Купить недвижимость"),
    KeyboardButton(text="🔑 Узнать срок сдачи дома")],
    [KeyboardButton(text="🗺 Где находится ЖК"),
    KeyboardButton(text="📱 Связаться с менеджером")],
    [KeyboardButton(text="ℹ Другое")]
]
MainMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=MainMenu)


# BuyMenu



BuyApartmentMenu = [
    [KeyboardButton(text="🏢 Квартира"),
    KeyboardButton(text="🏢 Коммерческое помещение")],
    [KeyboardButton(text="⬅ Главное меню")]
]
BuyApartmentMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=BuyApartmentMenu)



BuyCountryMenu = ReplyKeyboardBuilder()
for i in range(len(city)):
    BuyCountryMenu.button(text=f"🗺 {city[i]}").adjust(2)
BuyCountryMenu.row(MainMenuButton)


BuyKrasnodarMenu = ReplyKeyboardBuilder()
for i in range(len(krasnodar_jk)):
    BuyKrasnodarMenu.button(text=f"{krasnodar_jk[i]}").adjust(2)
BuyKrasnodarMenu.row(BackMenuButton,MainMenuButton)


BuyKaliningradMenu = ReplyKeyboardBuilder()
for i in range(len(kaliningrad_jk)):
    BuyKaliningradMenu.button(text=f"{kaliningrad_jk[i]}")
BuyKaliningradMenu.row(BackMenuButton,MainMenuButton)


BuyAnapaMenu = ReplyKeyboardBuilder()
for i in range(len(anapa_jk)):
    BuyAnapaMenu.button(text=f"{anapa_jk[i]}")
BuyAnapaMenu.row(BackMenuButton,MainMenuButton)


BuyMaikopMenu = ReplyKeyboardBuilder()
for i in range(len(maikop_jk)):
    BuyMaikopMenu.button(text=f"{maikop_jk[i]}")
BuyMaikopMenu.row(BackMenuButton,MainMenuButton)

BuyActionMenu = [
    [KeyboardButton(text="🔝 Топ предложений"),
     KeyboardButton(text="Все предложения")],
    [KeyboardButton(text="⬅ Назад"),
     KeyboardButton(text="⬅ Главное меню")]
]
BuyActionMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=BuyActionMenu)






#DateMenu

DateJKMenu = ReplyKeyboardBuilder()
for i in range(len(all_jk)):
    DateJKMenu.button(text=f"{all_jk[i]}")
DateJKMenu.adjust(2).row(MainMenuButton)







# GeoMenu


geo_krasnodar={'Сегодня':['г. Краснодар, ул. Ветеранов, 85',45.099318, 38.947713],
                    'Дом на Луговой':['г. Краснодар, ул. Луговая д. 7/6, п. г. т. Яблоновский',44.974029, 38.933326],
             'Дом на Московской':['г. Краснодар, ул. Московская, 112',45.077742, 39.002361],
                    'Ракурс':['г. Краснодар, ул. им. Героя Ростовского, 8',45.096388, 38.941594],
             'Жилой квартал Лучший':['г. Краснодар, ул. Петра Метальникова, 36',45.097246, 39.003062],
                    'Дыхание':['г. Краснодар, ул. Летчика Позднякова, 2',45.100720, 39.061066],
             'Свобода':['г. Краснодар, ул. Домбайская, 55',45.073344, 39.035617],
                    'Сердце':['г. Краснодар, ул. Школьная, 1',45.035509, 39.018154],
             'Фонтаны':['г. Краснодар, ул. Старокубанская, 2/23',45.002786, 39.032060],
                    'Открытие':['г. Краснодар, ул. Дубравная, 1',45.139732, 38.986677]}

geo_kaliningrad={'Включи':['г. Гурьевск, ул. Героя России Катериничева, з/у 2',54.759591, 20.596559]}

geo_anapa={'Песчаный':['г. Анапа, пр. Межсанаторный, 20к',44.939797, 37.318126],
                    'Аванта':['г. Анапа, ул. Крылова, д. 13',44.875886, 37.322073]}

geo_maikop={'Дружба':['г. Майкоп, ул. Степная 257',44.607186, 40.046794]}


GeoCountryMenu = ReplyKeyboardBuilder()
for i in range(len(city)):
    GeoCountryMenu.button(text=f"🗺 {city[i]}").adjust(2)
GeoCountryMenu.row(MainMenuButton)


GeoKrasnodarMenu = ReplyKeyboardBuilder()
for i in range(len(krasnodar_jk)):
    GeoKrasnodarMenu.button(text=f"{krasnodar_jk[i]}")
GeoKrasnodarMenu.adjust(2,2,2,2,2,1).row(BackMenuButton,MainMenuButton)


GeoKaliningradMenu = ReplyKeyboardBuilder()
for i in range(len(kaliningrad_jk)):
    GeoKaliningradMenu.button(text=f"{kaliningrad_jk[i]}")
GeoKaliningradMenu.adjust(1).row(BackMenuButton,MainMenuButton)



GeoAnapaMenu = ReplyKeyboardBuilder()
for i in range(len(anapa_jk)):
    GeoAnapaMenu.button(text=f"{anapa_jk[i]}")
GeoAnapaMenu.adjust(2).row(BackMenuButton,MainMenuButton)

GeoMaikopMenu = ReplyKeyboardBuilder()
for i in range(len(maikop_jk)):
    GeoMaikopMenu.button(text=f"{maikop_jk[i]}")
GeoMaikopMenu.adjust(2).row(BackMenuButton,MainMenuButton)



# support menu

SupportInlMenu = [
    [InlineKeyboardButton(text="В чат", callback_data="SupportChat", url="https://t.me/sskubansupportbot"),
     InlineKeyboardButton(text="Оставить заявку", callback_data="SupportApp")]
]
SupportInlMenu = InlineKeyboardMarkup(inline_keyboard=SupportInlMenu)

SupportCountryMenu = ReplyKeyboardBuilder()
for i in range(len(city)):
    SupportCountryMenu.button(text=f"🗺 {city[i]}").adjust(2)
SupportCountryMenu.row(MainMenuButton)



#referal_menu
ReferalMenu = [
    [KeyboardButton(text="👥 Узнать кол-во рефералов")],
     [KeyboardButton(text="⬅ Главное меню")]
]
ReferalMenu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=ReferalMenu)