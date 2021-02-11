class Route:
    """
    Class for handling Chess.com's API routes.

    Args:
        path(str): Path of route
    """
    BASE = 'https://api.chess.com/pub'
    """Chess.com's base API URL"""

    def __init__(self, path: str):
        self.path = path
        """Path for the URL route"""

        self.url = f'{self.BASE}/{self.path}'
        """URL"""
