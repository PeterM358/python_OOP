class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        current_player = [p for p in self.players if p == player]
        if current_player:
            return f"Player {player.name} is already in the guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        filtered_players = [p for p in self.players if p.name == player_name]
        if not filtered_players:
            return f"Player {player_name} is not in the guild."
        del self.players[player_name.index(player_name)]

        # player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players:
            result += p.player_info()

        return result
