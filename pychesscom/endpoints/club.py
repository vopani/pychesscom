from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Club:
    """
    Class for handling endpoints of club information.

    Args:
        client(BaseClient): HTTP client for API requests
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, url_id: str) -> Response:
        """
        Get profile details of a club.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-club-profile

        Args:
            url_id(str): The url_id of a club's web page on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.club.get_details('chess-com-developer-community')
            print(response)
        """
        route = Route(f'club/{url_id}')
        response = await self._client.request(route)

        return response

    async def get_members(self, url_id: str) -> Response:
        """
        Get members of a club.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-club-members

        Args:
            url_id(str): The url_id of a club's web page on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.club.get_members('chess-com-developer-community')
            print(response)
        """
        route = Route(f'club/{url_id}/members')
        response = await self._client.request(route)

        return response

    async def get_matches(self, url_id: str) -> Response:
        """
        Get team matches of a club.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-club-matches

        Args:
            url_id(str): The url_id of a club's web page on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.club.get_matches('chess-com-developer-community')
            print(response)
        """
        route = Route(f'club/{url_id}/matches')
        response = await self._client.request(route)

        return response
