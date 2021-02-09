from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Match:
    """
    Class for handling endpoints of team match information.

    :param client: HTTP client for API requests
    :type client: :class:`pychesscom.clients.base_client.BaseClient`
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, match_id: int) -> Response:
        """
        Get profile details of a team match.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-match-profile

        :param match_id: The match_id of a team match
        :type match_id: int
        :return: Response of API request
        :rtype: :class:`pychesscom.utils.response.Response`

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.match.get_details(12803)
            print(response)
        """
        route = Route(f'match/{match_id}')
        response = await self._client.request(route)

        return response

    async def get_board(self, match_id: int, board_id: int) -> Response:
        """
        Get board details of a team match.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-match-board

        :param match_id: The match_id of a team match
        :type match_id: int
        :param board_id: The board_id of a team match
        :type board_id: int
        :return: Response of API request
        :rtype: :class:`pychesscom.utils.response.Response`

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.match.get_board(12803, 1)
            print(response)
        """
        route = Route(f'match/{match_id}/{board_id}')
        response = await self._client.request(route)

        return response

    async def get_live_details(self, match_id: int) -> Response:
        """
        Get profile details of a live team match.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-match-live-profile

        :param match_id: The match_id of a live team match
        :type match_id: int
        :return: Response of API request
        :rtype: :class:`pychesscom.utils.response.Response`

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.match.get_live_details(5833)
            print(response)
        """
        route = Route(f'match/live/{match_id}')
        response = await self._client.request(route)

        return response

    async def get_live_board(self, match_id: int, board_id: int) -> Response:
        """
        Get board details of a live team match.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-endpoint-match-live-board

        :param match_id: The match_id of a live team match
        :type match_id: int
        :param board_id: The board_id of a live team match
        :type board_id: int
        :return: Response of API request
        :rtype: :class:`pychesscom.utils.response.Response`

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.match.get_live_board(5833, 1)
            print(response)
        """
        route = Route(f'match/live/{match_id}/{board_id}')
        response = await self._client.request(route)

        return response
