from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Tournament:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, url: str) -> Response:
        route = Route(f'tournament/{url}')
        response = await self._client.request(route)

        return response

    async def get_round(self, url: str, round: int) -> Response:
        route = Route(f'tournament/{url}/{round}')
        response = await self._client.request(route)

        return response

    async def get_round_group(self, url: str, round: int, group: int) -> Response:
        route = Route(f'tournament/{url}/{round}/{group}')
        response = await self._client.request(route)

        return response
