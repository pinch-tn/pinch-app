from django.conf.urls import patterns, include, url

import views

urls = patterns('',
                url("^poll/", views.poll))
