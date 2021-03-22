from project.base_repository import BaseRepository


class PlayerRepository(BaseRepository):
    @property
    def players(self):
        return self.values

    def get_identifier(self, player):
        return player.username

    def get_cannot_add_message(self, player):
        return f'Player {player.username} already exists!'

    def get_cannot_remove_message(self, obj):
        return f'Player cannot be an empty string!'
