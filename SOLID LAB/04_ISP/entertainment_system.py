# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass
#
#
# class Television(EntertainmentDevice):
#     def connect_to_dvd(self, dvd_player):
#         self.connect_to_device_via_rca_cable(dvd_player)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_hdmi_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class dvd_player(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class GameConsole(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def connect_to_router(self, router):
#         self.connect_to_device_via_ethernet_cable(router)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class Router(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_ethernet_cable(television)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_ethernet_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)


class HdmiConnectable:
    def connect_via_hdmi(self, device):
        return 'Connected via HDMI'


class RcaConnectable:
    def connect_via_rca(self, device):
        pass


class EthernetConnectable:
    def connect_via_ethernet(self, device):
        pass


class PowerOutletConnectable:
    def connect_to_power_outlet(self, device):
        pass


class EntertainmentDevice:
    pass


class Television(EntertainmentDevice, RcaConnectable, HdmiConnectable, PowerOutletConnectable):
    def connect_to_dvd(self, dvd_player):
        self.connect_via_rca(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_via_hdmi(game_console)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)

    def connect_via_hdmi(self, device):
        return None


tv = Television()


class DvdPlayer(EntertainmentDevice, HdmiConnectable, PowerOutletConnectable):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HdmiConnectable, EthernetConnectable, PowerOutletConnectable):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def connect_to_router(self, router):
        self.connect_via_ethernet(router)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetConnectable, PowerOutletConnectable):
    def connect_to_tv(self, television):
        self.connect_via_ethernet(television)

    def connect_to_game_console(self, game_console):
        self.connect_via_ethernet(game_console)

    def plug_in_power(self):
        self.connect_to_power_outlet(self)