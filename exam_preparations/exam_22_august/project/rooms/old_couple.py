from appliances.fridge import Fridge
from appliances.stove import Stove
from appliances.tv import TV
from rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    appliances_list = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, salary: float):
        pass