from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    heavy_type = 'Heavy'
    more_capacity_multiply = 2
    less_memory_multiply = 0.75

    def __init__(self, name, capacity, memory):
        super().__init__(name=name,
                         type=self.heavy_type,
                         capacity=int(capacity * self.more_capacity_multiply),
                         memory=int(memory * self.less_memory_multiply))
