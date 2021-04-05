class Room:
    family_name: str = ''
    budget: float = 0
    members_count: int = 0
    children: list = []

    def __init__(self, name: str, budget: float, members_count: int, *args):
        Room.family_name = name
        Room.budget = budget
        Room.members_count = members_count
        Room.children = [child for child in args] if args else []

    @staticmethod
    def calculate_expenses(*args):
        return sum(apps.cost for apps in args)

    @property
    def expenses(self):
        return self.expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.expenses = value





# young = AloneYoung('koki', 500)
# print([el.cost for el in young.appliances_list])