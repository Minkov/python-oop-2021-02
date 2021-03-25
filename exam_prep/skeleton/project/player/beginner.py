from project.player.player import Player


class Beginner(Player):
    initial_points = 50

    def __init__(self, username):
        super().__init__(username, self.initial_points)

    def increase_cards_damage(self, damage_increase):
        for card in self.card_repository.cards:
            card.damage_points += damage_increase

    def apply_cards_bonus(self):
        for card in self.card_repository.cards:
            self.health += card.health_points

    def apply_bonuses(self):
        self.health += 40
        self.increase_cards_damage(30)
        self.apply_cards_bonus()
