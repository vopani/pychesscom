from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Country:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, iso: str) -> Response:
        route = Route(f'country/{iso}')
        response = await self._client.request(route)

        return response

    async def get_players(self, iso: str) -> Response:
        route = Route(f'country/{iso}/players')
        response = await self._client.request(route)

        return response

    async def get_clubs(self, iso: str) -> Response:
        route = Route(f'country/{iso}/clubs')
        response = await self._client.request(route)

        return response
