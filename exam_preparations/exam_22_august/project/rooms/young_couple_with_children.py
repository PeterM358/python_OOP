from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    initial_members = 2
    room_cost = 30
    appliance_types = (TV(), Fridge(), Laptop())

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.room_members = self.initial_members + len(children)
        super().__init__(family_name, salary_one + salary_two, self.room_members)
        self.children = children
        self.calculate_expenses(self.appliances, children)




