from django.conf.urls import patterns, include, url

import views

urls = patterns('',
                url("^create_project/", views.CreateProjectView.as_view()),
                url("^big_idea/(?P<name>[A-Za-z0-9_-]+)/$", views.BigIdeaView.as_view()),
                url("^create_mvp/(?P<name>[A-Za-z0-9_-]+)/$", views.CreateMvpView.as_view()),
                url("^gravity_board/(?P<name>[A-Za-z0-9_-]+)/$", views.GravityBoardView.as_view()),
                url("^minify_mvp/(?P<name>[A-Za-z0-9_-]+)/$", views.MinifyMvpView.as_view()),
                url("^validate/(?P<name>[A-Za-z0-9_-]+)/$", views.ValidateView.as_view()),
                )
