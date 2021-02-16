from django.contrib.auth.models import AnonymousUser
from api.models import User


from typing import Callable, Any
from shortcuts import RequestType, HttpResponse


# class IPAccessMiddleware(object):
#     def process_request(self, request):
#         if request.user == AnonymousUser():
#             remoteip = request.META['REMOTE_ADDR']
#
#             User.get_or_create(ip=remoteip)
#
#             # try:
#             #     user = User.objects.get(ip=remoteip)
#             #     request.user = user
#             # except IPAccess.DoesNotExist:
#             #     # set_unusable_password
#             #     pass
#         return None

class IPAccessMiddleware:

    def __init__(self, get_response: Callable[[Any], Any]) -> None:

        self.get_response = get_response

    def __call__(self, request: RequestType) -> HttpResponse:

        if request.user == AnonymousUser():
            remote_ip = request.META['REMOTE_ADDR']
            user, _ = User.objects.get_or_create(ip=remote_ip)
            request.user = user

        response = self.get_response(request)

        return response
