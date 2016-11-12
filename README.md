fail-nicely-django
==================

An example Django project with nice logging settings for debugging failures.

![Bugs falling down](https://media.giphy.com/media/6WMXVZxdSIONW/giphy.gif)

Features
--------

- [x] stdout & rotating file logging
- [x] timestamps in the log format
- [ ] logs visible from runserver, gunicorn, uwsgi, systemd, honcho, Docker
- [x] deploy to Heroku button which just works with `heroku logs`
- [ ] show how to upgrade to Sentry

Tested in Django 1.9, but should work since 1.3, though 1.9 made
[some changes](https://docs.djangoproject.com/en/1.9/releases/1.9/#default-logging-changes-19)
to the default Django loggers.

Sample log file output:

```
2016-04-05 22:12:32,984 [Thread-1    ] [INFO ] [djangoproject.logger]  This is a manually logged INFO string.
2016-04-05 22:12:32,984 [Thread-1    ] [DEBUG] [djangoproject.logger]  This is a manually logged DEBUG string.
2016-04-05 22:12:32,984 [Thread-1    ] [ERROR] [django.request      ]  Internal Server Error: /
Traceback (most recent call last):
  File "/Users/kermit/.virtualenvs/fail-nicely-django/lib/python3.5/site-packages/django/core/handlers/base.py", line 149, in get_response
    response = self.process_exception_by_middleware(e, request)
  File "/Users/kermit/.virtualenvs/fail-nicely-django/lib/python3.5/site-packages/django/core/handlers/base.py", line 147, in get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Users/kermit/projekti/git/fail-nicely-django/djangoproject/brokenapp/views.py", line 12, in brokenview
    raise Exception('This is an exception raised in a view.')
Exception: This is an exception raised in a view.
```


Why?
----

Django by default seems to prefer not to write the things you log to it
anywhere. It instead lets its loggers shortly meditate on the messages sent
their way, after which they silently discard them.
The messages are simply disintegrated...
They evaporate into the circuitry's chasm of nothingness... They cease to be.


It somehow seems odd to have “the default” and
“it's probably not what you want” describe the same thing :smiley: ...

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

Second, if you do use loggers, the `runserver`/`gunicorn` process doesn't output
log messages in your console. Things like Docker kind of religiously depend on
the executable outputting its own log files to stdout,
so why not do it this way?

[Others](http://stackoverflow.com/questions/5739830/simple-log-to-file-example-for-django-1-3/7045981)
seem to be missing "complete working example code" for effectively using
Django's logging capabilities too.

For these reason and after having
[some problems of my own](https://github.com/benoitc/gunicorn/issues/1124#issuecomment-161990634)
getting Django/Flask, `gunicorn` and `supervisord`
to behave nicely with the log output, I started assembling
the best options I found into a nice example configuration. This is still
work in progress, so suggestions and patches are welcome :smiley:.


Can I try it?
-------------

To test the setup locally:

    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    python djangoproject/manage.py migrate
    python djangoproject/manage.py runserver

And in another tab admire your logs:

    tail -f djangoproject.log

To trigger some errors and log messages
just open/refresh <http://localhost:8000/>.

You can also try it on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

And you should be able to examine the logs after you refresh the page.

    heroku logs -t --app myherokuapp

Open <https://myherokuapp.herokuapp.com> in your browser
to generate some exceptions (substitute your real app name).


Nice, I want this!
------------------

Cool, then just copy the
[*djangoproject/djangoproject/logger.py*](https://github.com/metakermit/fail-nicely-django/blob/master/djangoproject/djangoproject/logger.py)
file to your project (into the same folder where your *settings.py* is located)
and add the following line to the bottom of your *settings.py* file:

    from .logger import LOGGING

Then in every part of your project where you wanna log something manually,
either import the logger like in
[*djangoproject/brokenapp/views.py*](https://github.com/metakermit/fail-nicely-django/blob/master/djangoproject/brokenapp/views.py).
Alternatively, if you want the logger name to be something other
than `djangoproject.logger`, add to the top of every module
where you want to log something:

    import logging
    logger = logging.getLogger(__name__)

That's it, rock on!

References
----------

- https://docs.djangoproject.com/en/1.9/topics/logging/
- https://docs.python.org/3.5/library/logging.config.html
- http://stackoverflow.com/questions/5739830/simple-log-to-file-example-for-django-1-3
- http://stackoverflow.com/questions/12942195/django-verbose-request-logging
