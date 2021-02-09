from pychesscom.clients.base_client import BaseClient
from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class Player:
    def __init__(self, client: BaseClient):
        self._client = client

    async def get_details(self, username: str) -> Response:
        route = Route(f'player/{username}')
        response = await self._client.request(route)

        return response

    async def get_stats(self, username: str) -> Response:
        route = Route(f'player/{username}/stats')
        response = await self._client.request(route)

        return response

    async def is_online(self, username: str) -> Response:
        route = Route(f'player/{username}/is-online')
        response = await self._client.request(route)

        return response

    async def get_clubs(self, username: str) -> Response:
        route = Route(f'player/{username}/clubs')
        response = await self._client.request(route)

        return response

    async def get_matches(self, username: str) -> Response:
        route = Route(f'player/{username}/matches')
        response = await self._client.request(route)

        return response

    async def get_tournaments(self, username: str) -> Response:
        route = Route(f'player/{username}/tournaments')
        response = await self._client.request(route)

        return response

    async def get_current_games(self, username: str) -> Response:
        route = Route(f'player/{username}/games')
        response = await self._client.request(route)

        return response

    async def get_current_games_to_move(self, username: str) -> Response:
        route = Route(f'player/{username}/games/to-move')
        response = await self._client.request(route)

        return response

    async def get_games_monthly_archive(self, username: str) -> Response:
        route = Route(f'player/{username}/games/archives')
        response = await self._client.request(route)

        return response

    async def get_games(self, username: str, year: int, month: int) -> Response:
        if month < 10:
            month = f'0{month}'

        route = Route(f'player/{username}/games/{year}/{month}')
        response = await self._client.request(route)

        return response

    async def get_titled_players(self, title: str) -> Response:
        route = Route(f'titled/{title}')
        response = await self._client.request(route)

        return response
