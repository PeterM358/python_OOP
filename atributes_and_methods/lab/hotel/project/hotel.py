from project.room import Room
# from atributes_and_methods.lab.hotel.project_14134.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def find_room(rooms, room_number):
        return list(filter(lambda room: room.number == room_number, rooms))[0]

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        result = self.find_room(self.rooms, room_number).take_room(people)

        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        result = self.find_room(self.rooms, room_number).free_room()
        if result:
            return result
        self.guests = 0

    def print_status(self):
        free_room_numbers = [str(r) for r in self.rooms if not r.is_taken]
        taken_room_numbers = [str(r) for r in self.rooms if r.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_room_numbers)}")
        print(f"Taken rooms: {', '.join(taken_room_numbers)}")


# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()


