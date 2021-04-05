class Hero:

    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f'{self.username} of type {self.__class__.__name__}' \
               f' has level {self.level}'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value



