from django.shortcuts import render

# Create your views here.
def brokenview(request):
    raise Exception(
        'This view is broken. '
        'It generates an error entry in djangoproject.log'
        )
