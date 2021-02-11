from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Puzzle:
    """
    Class for handling endpoints of puzzle information.

    Args:
        client(BaseClient): HTTP client for API requests
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_daily(self) -> Response:
        """
        Get daily puzzle.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-daily-puzzle

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.puzzle.get_daily()
            print(response)
        """
        route = Route('puzzle')
        response = await self._client.request(route)

        return response

    async def get_random(self) -> Response:
        """
        Get random puzzle.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-random-daily-puzzle

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.puzzle.get_random()
            print(response)
        """
        route = Route('puzzle/random')
        response = await self._client.request(route)

        return response
