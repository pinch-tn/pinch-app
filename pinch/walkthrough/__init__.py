from django.conf.urls import patterns, include, url

import views

urls = patterns('',
                url("^create_project/", views.CreateProjectView.as_view()),
                url("^big_idea/", views.BigIdeaView.as_view()),
                )
