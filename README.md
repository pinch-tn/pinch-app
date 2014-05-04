pinch-app
=========

Checkout [pinch](http://www.startpinching.com/).

We're making it an app!

![codeship status](https://www.codeship.io/projects/fbbc8ec0-b53b-0131-952c-5a246534b827/status)


getting started
===============

Create a virtualenv:

```
virtualenv --distribute pinch-env
```

Activate the virtualenv:

```
. ./pinch-env/bin/activate
```

Install requirements:

```
pip install -r requirements/local.txt
```

Setup Database:

```
pinch/manage.py syncdb
pinch/manage.py migrate
```

Add Test Data:

```
pinch/manage.py loaddata walkthrough/fixtures/test_data.json
```

Run server:

```
pinch/manage.py runserver
```

