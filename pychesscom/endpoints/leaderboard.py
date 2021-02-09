from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Leaderboard:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_leaderboards(self) -> Response:
        route = Route('leaderboards')
        response = await self._client.request(route)

        return response
