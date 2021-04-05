from rooms.room import Room


class AloneOld(Room):
    room_cost = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension)
        AloneOld.family_name = family_name
        AloneOld.budget = pension

