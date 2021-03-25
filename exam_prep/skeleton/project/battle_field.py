class BattleField:
    def fight(self, attacker, enemy):
        self.validate_dead_player(attacker)
        self.validate_dead_player(enemy)
        attacker.apply_bonuses()
        enemy.apply_bonuses()

        while not attacker.is_dead and not enemy.is_dead:
            self.attack(attacker, enemy)
            self.attack(enemy, attacker)

    @staticmethod
    def validate_dead_player(player):
        if player.is_dead:
            raise ValueError('Player is dead!')

    def attack(self, attacker, enemy):
        enemy.take_damage(attacker.damage)
