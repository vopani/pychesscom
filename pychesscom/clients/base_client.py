import json
from aiohttp import ClientSession
from asyncio import get_event_loop

from pychesscom.utils.response import Response
from pychesscom.utils.route import Route


class BaseClient:
    """
    Class for handling HTTP Client requests.

    Args:
        loop(AbstractEventLoop): Asyncio event loop
    """
    def __init__(self, loop=None) -> None:
        self.loop = get_event_loop() if loop is None else loop

    async def request(self, route: Route, **kwargs) -> Response:
        """
        HTTP request for a route.

        Args:
            route(Route): The route for API request

        Returns:
            Response: Response of API request
        """
        async with ClientSession(loop=self.loop) as session:
            async with session.get(url=route.url, **kwargs) as r:
                content = await r.read()

                try:
                    content = json.loads(content)
                except json.decoder.JSONDecodeError:
                    content = 'error'

                response = Response(
                    url=str(r.url),
                    code=r.status,
                    reason=r.reason,
                    content_type=r.content_type,
                    timestamp=r.raw_headers[0][1],
                    content=content
                )

                return response
