from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Puzzle:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_daily(self) -> Response:
        route = Route('puzzle')
        response = await self._client.request(route)

        return response

    async def get_random(self) -> Response:
        route = Route('puzzle/random')
        response = await self._client.request(route)

        return response
