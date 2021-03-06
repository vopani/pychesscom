import datetime

from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Player:
    """
    Class for handling endpoints of player information.

    Args:
        client(BaseClient): HTTP client for API requests
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, username: str) -> Response:
        """
        Get profile details of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_details('erik')
            print(response)
        """
        route = Route(f'player/{username}')
        response = await self._client.request(route)

        return response

    async def get_stats(self, username: str) -> Response:
        """
        Get stats of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-stats

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_stats('erik')
            print(response)
        """
        route = Route(f'player/{username}/stats')
        response = await self._client.request(route)

        return response

    async def get_online_status(self, username: str) -> Response:
        """
        Get online status of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-is-online

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_online_status('erik')
            print(response)
        """
        route = Route(f'player/{username}/is-online')
        response = await self._client.request(route)

        return response

    async def get_clubs(self, username: str) -> Response:
        """
        Get clubs of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-clubs

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_clubs('erik')
            print(response)
        """
        route = Route(f'player/{username}/clubs')
        response = await self._client.request(route)

        return response

    async def get_matches(self, username: str) -> Response:
        """
        Get team matches of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-matches

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_matches('erik')
            print(response)
        """
        route = Route(f'player/{username}/matches')
        response = await self._client.request(route)

        return response

    async def get_tournaments(self, username: str) -> Response:
        """
        Get tournaments of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-player-tournaments

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_tournaments('erik')
            print(response)
        """
        route = Route(f'player/{username}/tournaments')
        response = await self._client.request(route)

        return response

    async def get_current_games(self, username: str) -> Response:
        """
        Get current games of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-current

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_current_games('erik')
            print(response)
        """
        route = Route(f'player/{username}/games')
        response = await self._client.request(route)

        return response

    async def get_current_games_to_move(self, username: str) -> Response:
        """
        Get current games of a player where it is the player's turn to move.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-tomove

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_current_games_to_move('erik')
            print(response)
        """
        route = Route(f'player/{username}/games/to-move')
        response = await self._client.request(route)

        return response

    async def get_monthly_archive(self, username: str) -> Response:
        """
        Get monthly archives of a player.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive-list

        Args:
            username(str): The username of a player on chess.com

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_monthly_archive('erik')
            print(response)
        """
        route = Route(f'player/{username}/games/archives')
        response = await self._client.request(route)

        return response

    async def get_games(self, username: str, year: int, month: int) -> Response:
        """
        Get games of a player in a particular month.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive

        Args:
            username(str): The username of a player on chess.com
            year(int): Year of archive
            month(int): Month of archive

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_monthly_archive('erik', 2009, 10)
            print(response)
        """
        if month < 10:
            month = f'0{month}'

        route = Route(f'player/{username}/games/{year}/{month}')
        response = await self._client.request(route)

        return response

    async def get_titled_players(self, title: str) -> Response:
        """
        Get titled players..

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-titled

        Args:
            title(str): The title abbreviation

        Returns:
            Response: Response of API request

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.player.get_titled_players('GM')
            print(response)
        """
        route = Route(f'titled/{title}')
        response = await self._client.request(route)

        return response
