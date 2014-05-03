from django.conf.urls import patterns, include, url
from django.shortcuts import render, redirect

import views

urls = patterns('',
                # url("^$", redirect("create_project")),
                url("^$", views.CreateProjectView.as_view(), name="create_project"),
                url("^(?P<slug>[A-Za-z0-9_-]+)/big_idea/$", views.BigIdeaView.as_view(), name="big_idea"),
                url("^(?P<slug>[A-Za-z0-9_-]+)/create_mvp/$", views.CreateMvpView.as_view(), name="create_mvp"),
                url("^(?P<slug>[A-Za-z0-9_-]+)/gravity_board/$", views.GravityBoardView.as_view(), name="gravity_board"),
                url("^(?P<slug>[A-Za-z0-9_-]+)/minify_mvp/$", views.MinifyMvpView.as_view(), name="minify_mvp"),
                url("^(?P<slug>[A-Za-z0-9_-]+)/validate/$", views.ValidateView.as_view(), name="validate"),
                url("^(?P<slug>[A-Za-z0-9_-]+)/$", views.RootProjectView.as_view(), name="root_project"),
                )
