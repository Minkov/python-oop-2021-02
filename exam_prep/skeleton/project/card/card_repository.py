from project.base_repository import BaseRepository


class CardRepository(BaseRepository):

    @property
    def cards(self):
        return self.values

    def get_identifier(self, card):
        return card.name

    def get_cannot_add_message(self, card):
        return f'Card {card.name} already exists!'

    def get_cannot_remove_message(self, obj):
        return f'Card cannot be an empty string!'
