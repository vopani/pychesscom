class Route:
    BASE = 'https://api.chess.com/pub'

    def __init__(self, path):
        self.path = path
        self.url = f'{self.BASE}/{self.path}'
