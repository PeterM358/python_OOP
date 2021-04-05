# from atributes_and_methods.exe.movie_world.project__.customer import Customer
# from atributes_and_methods.exe.movie_world.project__.dvd import DVD

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c._id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd._id == dvd_id][0]
        if dvd_id in [dvd._id for dvd in customer.rented_dvds]:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c._id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd._id == dvd_id][0]
        if dvd not in customer.rented_dvds:
            return f'{customer.name} does not have that DVD'
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f'{customer.name} has successfully returned {dvd.name}'

    def __repr__(self):
        a = 5
        result = '\n'.join([repr(c) for c in self.customers])
        result += '\n' + '\n'.join([repr(d) for d in self.dvds])
        return result


# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)


# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# movie_world.rent_dvd(4, 1)
# result = movie_world.rent_dvd(4, 1)


# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# movie_world.rent_dvd(4, 1)
# result = movie_world.return_dvd(4, 1)
# print(result)
