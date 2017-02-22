from django.shortcuts import render
from django.http import HttpResponse

from djangoproject.logger import log

# Create your views here.
def brokenview(request):
    # first, intentionally log something
    log.info('This is a manually logged INFO string.')
    log.debug('This is a manually logged DEBUG string.')
    # then have the view raise an exception (e.g. something went wrong)
    raise Exception('This is an exception raised in a view.')
    #return HttpResponse('hello')
