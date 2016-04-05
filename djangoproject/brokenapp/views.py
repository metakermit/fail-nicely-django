from django.shortcuts import render
from django.http import HttpResponse

from djangoproject.logger import logger

# Create your views here.
def brokenview(request):
    # first, intentionally log something
    logger.info('This is a manually logged INFO string.')
    logger.debug('This is a manually logged DEBUG string.')
    # then have the view raise an exception (e.g. something went wrong)
    raise Exception('This is an exception raised in a view.')
    #return HttpResponse('hello')
