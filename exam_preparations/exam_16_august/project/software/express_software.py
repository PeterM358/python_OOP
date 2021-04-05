from project.software.software import Software


class ExpressSoftware(Software):
    more_consumption = 2
    light_type = 'Express'

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name=name,
                         type=self.light_type,
                         capacity_consumption=capacity_consumption,
                         memory_consumption=int(memory_consumption * self.more_consumption))

#     def __repr__(self):
#         return f'{self.__dict__}' # TODO just for check. TO be writen correct
#
#
# print(ExpressSoftware('asd', 10, 10))