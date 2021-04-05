# from project.software.light_software import LightSoftware
from project.software.software import Software


class Hardware:

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    # @property
    # def available_memory(self):
    #     return self.memory - sum(m.memory_consumption for m in self.software_components)
    #
    # @property
    # def available_capacity(self):
    #     return self.capacity - sum(c.capacity_consumption for c in self.software_components)
    #
    # def install(self, software):
    #     if software.capacity_consumption <= self.available_capacity\
    #             and software.memory_consumption <= self.available_memory:
    #         self.software_components.append(software)
    #     else:
    #         raise Exception('Software cannot be installed')

    #################
    #################

    def valid_install(self, memory_needed, capacity_needed):
        total_memory_needed = sum(m.memory_consumption for m in self.software_components) + memory_needed
        total_capacity_needed = sum(c.capacity_consumption for c in self.software_components) + capacity_needed
        if total_memory_needed <= self.memory\
                and total_capacity_needed <= self.capacity:
            return True
        return False

    def install(self, software):
        if not self.valid_install(software.memory_consumption, software.capacity_consumption):
            raise Exception('Software cannot be installed')
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

