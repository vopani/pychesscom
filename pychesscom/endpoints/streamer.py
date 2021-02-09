from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Streamer:
    """
    Class for handling endpoints of streamer information.

    :param client: HTTP client for API requests
    :type client: :class:`pychesscom.clients.base_client.BaseClient`
    """
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_streamers(self) -> Response:
        """
        Get streamers.

        Chess.com API: https://www.chess.com/news/view/published-data-api#pubapi-streamers

        :return: Response of API request
        :rtype: :class:`pychesscom.utils.response.Response`

        Example:

        .. code-block:: python

            from pychesscom import ChessComClient
            client = ChessComClient()
            response = await client.streamer.get_streamers()
            print(response)
        """
        route = Route('streamers')
        response = await self._client.request(route)

        return response
