from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f'Monthly consumption: {sum(room.expenses + room.room_cost for room in self.rooms):.2f}$.'

    def pay(self):
        room_result = [self.__pay_for__room(room) for room in self.rooms]
        return '\n'.join(room_result)

    def __pay_for__room(self, room):
        if room.budget < room.total_expenses:
            self.rooms.remove(room)
            return f'{room.family_name} does not have enough budget and must leave the hotel.'
        room.budget -= room.total_expenses
        return f'{room.family_name} paid {room.total_expenses:.2f}$ and have {room.budget:.2f}$ left.'

    def status(self):
        rooms_result = [str(room) for room in self.rooms]
        result = [
            f'Total population: {self.__get_total_population}',
            *rooms_result,
        ]

        return '\n'.join(result)

    @property
    def __get_total_population(self):
        return sum(room.members_count for room in self.rooms)

