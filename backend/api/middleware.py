import datetime

from typing import Callable, Any
from shortcuts import RequestType, HttpResponse

from django.core.cache import cache
from django.conf import settings



class OnlineUserMiddleware:

    def __init__(self, get_response: Callable[[Any], Any]) -> None:

        self.get_response = get_response

    def __call__(self, request: RequestType) -> HttpResponse:

        if request.user.is_authenticated:
            now = datetime.datetime.now()
            cache.set('last_seen_%s' % request.user.id, now, settings.USER_LASTSEEN_TIMEOUT)

        response = self.get_response(request)

        return response
