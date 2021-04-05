from appliances.tv import TV
from rooms.room import Room


class AloneYoung(Room):
    room_cost = 10
    appliances_list = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary)
        AloneYoung.family_name = family_name
        AloneYoung.budget = salary

    def expenses(self):
        return sum(el.cost for el in AloneYoung.appliances_list)


# young = AloneYoung('koki', 500)
# print([el.cost for el in young.appliances_list])