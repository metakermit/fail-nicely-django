fail-nicely-django
==================

*An example Django project with nice logging settings for debugging failures.*

Desired features:

- [] stdout & rotating file logging
- [x] timestamps in the log format
- [] show how to upgrade to Sentry
- [] logs visible from runserver, gunicorn, uwsgi, systemd, honcho, Docker

Tested in Django 1.9, but should work since 1.3, though 1.9 made some changes
to the default Django loggers described
[here](https://docs.djangoproject.com/en/1.9/releases/1.9/#default-logging-changes-19).


Why?
----

Django by default seems to prefer not to write the things you log to it
anywhere. It instead lets its loggers shortly meditate on the messages sent
their way, after which they silently discard them.
The messages are simply disintegrated...
They evaporate into the circuitry's chasm of nothingness... They cease to be.


It somehow seems odd to have “the default” and
“it's probably not what you want” describe the same thing :) ...

> “If the disable_existing_loggers key in the LOGGING dictConfig is set to True
(which is the default) then all loggers from the default configuration will be
disabled. Disabled loggers are not the same as removed; the logger will still
exist, but will silently discard anything logged to it, not even propagating
entries to a parent logger. Thus you should be very careful using
'disable_existing_loggers': True; it’s probably not what you want.
Instead, you can set disable_existing_loggers to False and redefine
some or all of the default loggers [...].”
>
>  — Excerpt From: The Official Django Documentation

Second, if you do use loggers, the `manage.py runserver` command doesn't output
them in your console. Things like Docker kind of religiously depend on the
executable outputting its own log files to stdout, so why not do it this way?


Can I try it?
-------------

To test the setup locally:

    cd djangoproject
    # TODO: pip install -r requirements.txt
    python manage.py runserver


Nice, I want this!
------------------

Cool, then just check out the *djangoproject/settings.py* file
and copy the `LOGGING` setting to your *settings.py* file.


References
----------

- https://docs.djangoproject.com/en/1.9/topics/logging/
- https://docs.python.org/3.5/library/logging.config.html
- http://stackoverflow.com/questions/5739830/simple-log-to-file-example-for-django-1-3
- http://stackoverflow.com/questions/12942195/django-verbose-request-logging
