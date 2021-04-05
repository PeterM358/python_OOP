from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from typing import List

from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        try:
            hardware_exist = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware_exist.install(software)
            System._software.append(software)
        except IndexError:
            return 'Hardware does not exist'
        except Exception as ex:
            return str(ex)

        # hardware_exist = [h for h in System._hardware if h.name == hardware_name]
        # if not hardware_exist:
        #     return 'Hardware does not exist'
        # try:
        #     software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        #     hardware_exist[0].install(software)
        #     System._software.append(software)
        # except Exception as ex:
        #     return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_exist = [h for h in System._hardware if h.name == hardware_name]
        if not hardware_exist:
            return 'Hardware does not exist'
        try:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware_exist[0].install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware_exist = [h for h in System._hardware if h.name == hardware_name][0]
            software_exist = [s for s in System._software if s.name == software_name][0]
            hardware_exist.uninstall(software_exist)
            System._software.remove(software_exist)
        except IndexError:
            return 'Some of the components do not exist'
        except Exception as ex:
            return str(ex)

    @staticmethod
    def get_total_memory(hardwares):
        return sum(h.memory for h in hardwares)

    @staticmethod
    def get_total_used_memory(softwares):
        return sum(s.memory_consumption for s in softwares)

    @staticmethod
    def get_total_used_space(softwares):
        return sum(s.capacity_consumption for s in softwares)

    @staticmethod
    def get_total_space(hardwares):
        return sum(h.capacity for h in hardwares)

    @staticmethod
    def get_hardwares():
        return [h for h in System._hardware]

    @staticmethod
    def get_softwares():
        return [s for s in System._software]

    @staticmethod
    def analyze():
        count_hardware = len(System._hardware)
        count_software = len(System._software)
        hardwares = System.get_hardwares()
        softwares = System.get_softwares()
        total_memory = System.get_total_memory(hardwares)
        total_used_memory = System.get_total_used_memory(softwares)
        total_space = System.get_total_space(hardwares)
        total_used_space = System.get_total_used_space(softwares)

        return f"System Analysis\n" \
               f"Hardware Components: {count_hardware}\n" \
               f"Software Components: {count_software}\n" \
               f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {total_used_space} / {total_space}"

    @staticmethod
    def system_split():
        result = ''
        for hard in System._hardware:
            result += f'Hardware Component - {hard.name}\n'
            express_software_components = [s for s in hard.software_components if s.__class__.__name__ == 'ExpressSoftware']
            result += f'Express Software Components: {len(express_software_components)}\n'
            light_software_components = [s for s in hard.software_components if s.__class__.__name__ == 'LightSoftware']
            result += f'Light Software Components: {len(light_software_components)}\n'
            result += f'Memory Usage: {sum(s.memory_consumption for s in hard.software_components)} / {hard.memory}\n'
            result += f'Capacity Usage: {sum(s.capacity_consumption for s in hard.software_components)} / {hard.capacity}\n'
            result += f'Type: {hard.type}\n'
            names = ', '.join(s.name for s in hard.software_components)
            result += f'Software Components: {names if names else None}'
        return result
