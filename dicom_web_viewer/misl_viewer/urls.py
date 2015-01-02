# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from misl_viewer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),   # home
    url(r'^upload/$', views.upload, name='upload'),  # 保存
    url(r'^list/$', views.list, name='list'),  #一覧
    url(r'^test/$', views.test, name='test'),  #一覧
#    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
#    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除

)
