from app.controllers.goodreads import api
from fastack import ReadOnlyController
from fastack.decorators import route
from fastapi import Request, Response
from pydantic import conint

from fastack_cache.backends.aioredis import AioRedisBackend
from fastack_cache.decorators import cached


class GoodreadsController(ReadOnlyController):
    async def list(
        self,
        request: Request,
        q: str,
        page: conint(gt=0) = 1,
        page_size: conint(gt=0) = 10,
    ) -> Response:
        cache: AioRedisBackend = request.state.cache
        async with cache:
            quotes = await cache.get(q)
            if not quotes:
                quotes = await api.get_quotes(q)
                await cache.set(q, quotes, 15)

            return self.get_paginated_response(quotes, page, page_size)

    @route("/{tag}")
    @cached()
    async def retrieve(self, request: Request, tag: str) -> Response:
        quotes = await api.get_quotes(tag)
        return self.json(f"{tag} quote", quotes)
