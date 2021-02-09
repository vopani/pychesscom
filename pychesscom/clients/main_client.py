from pychesscom.clients.base_client import BaseClient
from pychesscom.endpoints.club import Club
from pychesscom.endpoints.country import Country
from pychesscom.endpoints.leaderboard import Leaderboard
from pychesscom.endpoints.match import Match
from pychesscom.endpoints.player import Player
from pychesscom.endpoints.puzzle import Puzzle
from pychesscom.endpoints.streamer import Streamer
from pychesscom.endpoints.tournament import Tournament


class ChessComClient:
    """
    Class for handling Chess.com API requests.

    :param loop: Asyncio event loop
    :type loop: :class:`asyncio.AbstractEventLoop`

    Example:

    .. code-block:: python

        from pychesscom import ChessComClient
        client = ChessComClient()
    """
    def __init__(self, loop=None) -> None:
        self._client = BaseClient(loop=loop)
        self.club = Club(client=self._client)
        self.country = Country(client=self._client)
        self.leaderboard = Leaderboard(client=self._client)
        self.match = Match(client=self._client)
        self.player = Player(client=self._client)
        self.puzzle = Puzzle(client=self._client)
        self.streamer = Streamer(client=self._client)
        self.tournament = Tournament(client=self._client)
