from django.conf.urls import patterns, include, url

import views

urls = patterns('',
                url("^create_project/", views.CreateProjectView.as_view()),
                url("^big_idea/", views.BigIdeaView.as_view()),
                url("^create_mvp/", views.create_mvp),
                url("^gravity_board/", views.gravity_board),
                url("^minify_mvp/", views.minify_mvp),
                url("^validate/", views.validate),
                )
