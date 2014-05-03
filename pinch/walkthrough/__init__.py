from django.conf.urls import patterns, include, url
from django.shortcuts import render, redirect

import views

urls = patterns('',
                url("^$", redirect("create_project")),
                url("^(?P<name>[A-Za-z0-9_-]+)/$", views.RootProjectView.as_view(), name="root_project"),
                url("^create_project/$", views.CreateProjectView.as_view(), name="create_project"),
                url("^big_idea/(?P<name>[A-Za-z0-9_-]+)/$", views.BigIdeaView.as_view(), name="big_idea"),
                url("^create_mvp/(?P<name>[A-Za-z0-9_-]+)/$", views.CreateMvpView.as_view(), name="create_mvp"),
                url("^gravity_board/(?P<name>[A-Za-z0-9_-]+)/$", views.GravityBoardView.as_view(), name="gravity_board"),
                url("^minify_mvp/(?P<name>[A-Za-z0-9_-]+)/$", views.MinifyMvpView.as_view(), name="minify_mvp"),
                url("^validate/(?P<name>[A-Za-z0-9_-]+)/$", views.ValidateView.as_view(), name="validate"),
                )
