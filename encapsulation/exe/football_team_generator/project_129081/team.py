class Team:

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    def add_player(self, player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        try:
            player = [p for p in self.players if p.name == player_name][0]
            temp = player
            self.players.remove(player)
            return temp
        except IndexError:
            return f'Player {player_name} not found'


