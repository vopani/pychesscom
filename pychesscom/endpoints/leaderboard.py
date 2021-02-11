from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Leaderboard:
    """
    Class for handling endpoints of leaderboard information.

    Args:
        client(BaseClient): HTTP client for API requests
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_leaderboards(self) -> Response:
        """
        Get top-50 players of leaderboards.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-leaderboards

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.leaderboard.get_leaderboards()
            print(response)
        """
        route = Route('leaderboards')
        response = await self._client.request(route)

        return response
