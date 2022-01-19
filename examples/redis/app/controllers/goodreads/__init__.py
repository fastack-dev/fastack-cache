from app.controllers.goodreads import api
from fastack import ReadOnlyController
from fastack.decorators import route
from fastack.globals import request
from fastapi import Request, Response
from pydantic import conint

from fastack_cache.backends.redis import RedisBackend
from fastack_cache.decorators import cached
from fastack_cache.helpers import run_sync


class GoodreadsController(ReadOnlyController):
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

    @route("/{tag}")
    @cached()
    def retrieve(self, tag: str) -> Response:
        quotes = run_sync(api.get_quotes, tag)
        return self.json(f"{tag} quote", quotes)
