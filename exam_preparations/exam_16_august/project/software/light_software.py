from project.software.software import Software


class LightSoftware(Software):
    more_capacity = 1.5
    lesser_memory = 0.5
    light_type = 'Light'

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name=name,
                         type=self.light_type,
                         capacity_consumption=int(capacity_consumption * self.more_capacity),
                         memory_consumption=int(memory_consumption * self.lesser_memory))


#     def __repr__(self):
#         return f'{self.__dict__}' # TODO just for check. TO be writen correct or comment
#
# ls = LightSoftware('asd', 10, 10)
# print(ls)