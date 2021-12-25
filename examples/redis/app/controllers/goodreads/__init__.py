from app.controllers.goodreads import api
from fastack import ListController
from fastapi import Request, Response
from pydantic import conint

from fastack_cache.backends.redis import RedisBackend


class GoodreadsController(ListController):
    async def list(
        self,
        request: Request,
        q: str,
        page: conint(gt=0) = 1,
        page_size: conint(gt=0) = 10,
    ) -> Response:
        cache: RedisBackend = request.state.cache
        with cache:
            quotes = cache.get(q)
            if not quotes:
                quotes = await api.get_quotes(q)
                cache.set(q, quotes, 15)

            return self.get_paginated_response(quotes, page, page_size)
