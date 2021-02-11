from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Country:
    """
    Class for handling endpoints of country information.

    Args:
        client(BaseClient): HTTP client for API requests
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, iso: str) -> Response:
        """
        Get profile details of a country.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-country-profile

        Args:
            iso(str): 2-character ISO 3166 code of country

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.country.get_details('IT')
            print(response)
        """
        iso = iso.upper()

        route = Route(f'country/{iso}')
        response = await self._client.request(route)

        return response

    async def get_players(self, iso: str) -> Response:
        """
        Get players of a country.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-country-players

        Args:
            iso(str): 2-character ISO 3166 code of country

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.country.get_players('IT')
            print(response)
        """
        iso = iso.upper()

        route = Route(f'country/{iso}/players')
        response = await self._client.request(route)

        return response

    async def get_clubs(self, iso: str) -> Response:
        """
        Get clubs of a country.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-country-clubs

        Args:
            iso(str): 2-character ISO 3166 code of country

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.country.get_clubs('IT')
            print(response)
        """
        iso = iso.upper()

        route = Route(f'country/{iso}/clubs')
        response = await self._client.request(route)

        return response
