from __future__ import absolute_import, division, print_function

from django.utils.deprecation import MiddlewareMixin

import logging
log = logging.getLogger(__name__)

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_request():
    """ returns the request object for this thread """
    print("get current request")
    return getattr(_thread_locals, "request", None)

def get_current_user():
    """ returns the current user, if exist, otherwise returns None """
    print("get current user")
    request = get_current_request()
    log.info("request %s: ", request)

    if request:
        return getattr(request, "user", None)

class ThreadLocalMiddleware(MiddlewareMixin):
    """ Simple middleware that adds the request object in thread local storage."""

    def process_request(self, request):
        print("Processing request")
        _thread_locals.request = request

    def process_response(self, request, response):
        print("Processing response")
        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request
        return response