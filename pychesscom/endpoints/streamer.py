from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Streamer:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_streamers(self) -> Response:
        route = Route('streamers')
        response = await self._client.request(route)

        return response
