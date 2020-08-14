class Sound:
    def __init__(self, category: str, identifier: str, repeat: int = 1):
        self.category = category
        self.identifier = identifier
        self.repeat = repeat

    def to_json(self) -> dict:
        return {'category': self.category, 'id': self.identifier, 'repeat': self.repeat}
