import os
import logging

from .settings import BASE_DIR

# the basic logger other apps can import
logger = logging.getLogger(__name__)

# Note, doing this manually in every module results in nicer output:
#
#     import logging
#     logger = logging.getLogger(__name__)

# logging dictConfig configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, # keep Django's default loggers
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'timestampthread': {
            'format': "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(filepath)s:%(lineno)s]  %(message)s",
        },
    },
    'handlers': {
        'logfile': {
            # optionally raise to INFO to not fill the log file too quickly
            'level': 'DEBUG', # DEBUG or higher goes to the log file
            'class':'logging.handlers.RotatingFileHandler',
            # IMPORTANT: replace with your desired logfile name!
            'filename': os.path.join(BASE_DIR, 'djangoproject.log'),
            'maxBytes': 50 * 10**6, # will 50 MB do?
            'backupCount': 3, # keep this many extra historical files
            'formatter': 'timestampthread'
        },
        'console': {
            'level': 'DEBUG', # DEBUG or higher goes to the console
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': { # configure all of Django's loggers
            'handlers': ['logfile', 'console'],
            'level': 'INFO', # set to debug to see e.g. database queries
            'propagate': False, # don't propagate further, to avoid duplication
        },
        # root configuration – for all of our own apps
        # (feel free to do separate treatment for e.g. brokenapp vs. sth else)
        '': {
            'handlers': ['logfile', 'console'],
            'level': 'DEBUG',
        },
    },
}
