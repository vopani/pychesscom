from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Club:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, url: str) -> Response:
        route = Route(f'club/{url}')
        response = await self._client.request(route)

        return response

    async def get_members(self, url: str) -> Response:
        route = Route(f'club/{url}/members')
        response = await self._client.request(route)

        return response

    async def get_matches(self, url: str) -> Response:
        route = Route(f'club/{url}/matches')
        response = await self._client.request(route)

        return response
