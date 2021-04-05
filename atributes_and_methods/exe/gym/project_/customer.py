from atributes_and_methods.exe.gym.project_.equipment import Equipment
from atributes_and_methods.exe.gym.project_.exercise_plan import ExercisePlan
from atributes_and_methods.exe.gym.project_.gym import Gym
from atributes_and_methods.exe.gym.project_.subscription import Subscription
from atributes_and_methods.exe.gym.project_.trainer import Trainer


class Customer:
    customer_id = 0

    def __init__(self, name, address, email):
        Customer.customer_id += 1
        self.name = name
        self.address = address
        self.email = email
        self._id = Customer.customer_id

    def __repr__(self):
        return f"Customer <{self._id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.customer_id + 1

#
# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))

