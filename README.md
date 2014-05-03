pinch-app
=========

Checkout [pinch](http://www.startpinching.com/).

We're making it an app!


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

