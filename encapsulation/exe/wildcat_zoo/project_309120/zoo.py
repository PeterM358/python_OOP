# from encapsulation.exe.wildcat_zoo.project_309120.caretaker import Caretaker
# from encapsulation.exe.wildcat_zoo.project_309120.cheetah import Cheetah
# from encapsulation.exe.wildcat_zoo.project_309120.keeper import Keeper
# from encapsulation.exe.wildcat_zoo.project_309120.lion import Lion
# from encapsulation.exe.wildcat_zoo.project_309120.tiger import Tiger
# from encapsulation.exe.wildcat_zoo.project_309120.vet import Vet

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return f'Not enough space for animal'
        if price > self.__budget:
            return f'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        # обдж.__клас__.наме взимаме стр(Името на класа)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not len(self.workers) < self.__workers_capacity:
            return f'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f'{worker.name} fired successfully'
        except IndexError:
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])
        # for worker_lab in self.workers:
        #     total_salaries += worker_lab.salary
        if self.__budget < total_salaries:
            return f'You have no budget to pay your workers. They are unhappy'
        self.__budget -= total_salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        total_costs = sum([a.get_needs() for a in self.animals])
        if total_costs > self.__budget:
            return 'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= total_costs
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [li for li in self.animals if li.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(lions)} Lions:\n'
        #  -> Не става \n
        # result += f"{'\n'.join([repr(l) for l in lions])}"
        # така вече става
        result += '{}'.format('\n'.join([repr(li) for li in lions])) + '\n'

        result += f'----- {len(tigers)} Tigers:\n'
        result += '{}'.format('\n'.join([repr(t) for t in tigers])) + '\n'

        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '{}'.format('\n'.join([repr(c) for c in cheetahs]))

        return result

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']

        result = f"You have {len(self.workers)} workers\n"
        result += f'----- {len(keepers)} Keepers:\n'
        result += '{}'.format('\n'.join([repr(k) for k in keepers])) + '\n'

        result += f'----- {len(caretakers)} Caretakers:\n'
        result += '{}'.format('\n'.join([repr(c) for c in caretakers])) + '\n'

        result += f'----- {len(keepers)} Vets:\n'
        result += '{}'.format('\n'.join([repr(v) for v in vets]))

        return result



# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker_lab in workers:
#     print(zoo.hire_worker(worker_lab))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker_lab
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())