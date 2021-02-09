from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Match:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, match_id: int) -> Response:
        route = Route(f'match/{match_id}')
        response = await self._client.request(route)

        return response

    async def get_board(self, match_id: int, board_id: int) -> Response:
        route = Route(f'match/{match_id}/{board_id}')
        response = await self._client.request(route)

        return response

    async def get_live(self, match_id: int) -> Response:
        route = Route(f'match/live/{match_id}')
        response = await self._client.request(route)

        return response

    async def get_live_board(self, match_id: int, board_id: int) -> Response:
        route = Route(f'match/live/{match_id}/{board_id}')
        response = await self._client.request(route)

        return response
