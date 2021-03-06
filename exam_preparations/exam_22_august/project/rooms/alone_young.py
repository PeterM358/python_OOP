from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_cost = 10
    default_members = 1
    appliance_types = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.default_members)
        self.calculate_expenses(self.appliances)


# young = AloneYoung('koki', 500)
# print([el.cost for el in young.appliances_list])