from appliances.appliance import Appliance


class TV(Appliance):

    def __init__(self):
        super().__init__(cost=1.5)

    # just for check
    # def __repr__(self):
    #     return f'{self.__dict__}'
