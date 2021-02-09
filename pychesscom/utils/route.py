class Route:
    """
    Class for handling Chess.com's API routes.

    :param path: Path of route
    :type path: str
    """
    BASE = 'https://api.chess.com/pub'
    """Chess.com's base API URL"""

    def __init__(self, path):
        self.path = path
        self.url = f'{self.BASE}/{self.path}'
