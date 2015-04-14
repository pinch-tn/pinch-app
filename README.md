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
pinch/manage.py loaddata pinch/walkthrough/fixtures/test_data.json
```

Run server:

```
pinch/manage.py runserver
```

development
===========

I'm just including some handy tips here for development purposes.

### updating the models

Whenever you make a change to the models in Django, we will need to change the database. More importantly, we need to change the database in a way that doesn't lose production data. So that means two things:

1. Don't make huge, schema-rewrite type changes. Stick to small, incremental ones.
2. Update the migrations after you make changes.

        pinch/manage.py schemamigrations walkthrough --auto
   If this goes off without any trouble (it usually will), you're good. Otherwise, consult the [relevant *south* documentation][1].

[1]: http://south.readthedocs.org/en/latest/tutorial/part2.html#tutorial-part-2 "South: Advanced Changes"


