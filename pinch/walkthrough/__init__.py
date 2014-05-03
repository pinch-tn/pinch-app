from django.conf.urls import patterns, include, url

import views

urls = patterns('',
                url("^create_project/", views.create_project),
                url("^big_idea/", views.big_idea),
                )
