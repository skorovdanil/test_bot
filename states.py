from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    info_block = State()
    buy = State()

    buy_ap = State()
    buy_ap_city = State()
    buy_ap_jk = State()
    buy_ap_rooms_count = State()
    buy_ap_room = State()
    buy_ap_room_menu = State()
    buy_ap_room_action = State()
    buy_ap_room_floors = State()
    buy_ap_room_end = State()
    buy_ap_room_end_firstname = State()
    buy_ap_room_end_telephone = State()


    buy_comm = State()
    buy_comm_city = State()
    buy_comm_jk = State()
    buy_comm_rooms_count = State()
    buy_comm_room = State()
    buy_comm_room_menu = State()
    buy_comm_room_action = State()
    buy_comm_room_floors = State()
    buy_comm_room_end = State()
    buy_comm_room_end_firstname = State()
    buy_comm_room_end_telephone = State()

    rooms_count = State()


    date = State()
    date_jk = State()


    geo = State()
    geo_city = State()
    geo_jk = State()

    support_country = State()
    support_app = State()



    ref_start = State()
    ref_menu = State()
