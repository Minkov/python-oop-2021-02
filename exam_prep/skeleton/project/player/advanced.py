from project.player.player import Player


class Advanced(Player):
    initial_points = 250

    def __init__(self, username):
        super().__init__(username, self.initial_points)

    def apply_bonuses(self):
        pass
