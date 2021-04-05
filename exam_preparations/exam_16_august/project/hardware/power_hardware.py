from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    power_type = 'Power'
    less_capacity_multiply = 0.25
    more_memory_multiply = 0.75

    def __init__(self, name, capacity, memory):
        super().__init__(name=name,
                         type=self.power_type,
                         capacity=int(capacity * self.less_capacity_multiply),
                         memory=int(memory + memory*self.more_memory_multiply))

