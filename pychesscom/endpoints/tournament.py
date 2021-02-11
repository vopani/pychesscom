from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Tournament:
    """
    Class for handling endpoints of tournament information.

    Args:
        client(BaseClient): HTTP client for API requests
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, url_id: str) -> Response:
        """
        Get profile details of a tournament.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-tournament-profile

        Args:
            url_id(str): The url_id of a tournament's web page on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.tournament.get_details('-33rd-chesscom-quick-knockouts-1401-1600')
            print(response)
        """
        route = Route(f'tournament/{url_id}')
        response = await self._client.request(route)

        return response

    async def get_round(self, url_id: str, round_id: int) -> Response:
        """
        Get round details of a tournament.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-tournament-round

        Args:
            url_id(str): The url_id of a tournament's web page on chess.com
            round_id(int): The round_id of a tournament

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.tournament.get_round('-33rd-chesscom-quick-knockouts-1401-1600', 1)
            print(response)
        """
        route = Route(f'tournament/{url_id}/{round_id}')
        response = await self._client.request(route)

        return response

    async def get_round_group(self, url_id: str, round_id: int, group_id: int) -> Response:
        """
        Get group details of a tournament round.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-tournament-round-group

        Args:
            url_id(str): The url_id of a tournament's web page on chess.com
            round_id(int): The round_id of a tournament
            group_id(int): The group_id of a tournament round

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.tournament.get_round_group('-33rd-chesscom-quick-knockouts-1401-1600', 1, 1)
            print(response)
        """
        route = Route(f'tournament/{url_id}/{round_id}/{group_id}')
        response = await self._client.request(route)

        return response
