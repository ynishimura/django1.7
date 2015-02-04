# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from misl_viewer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),   # home
    url(r'^upload/$', views.Upload, name='upload'),  # 保存
    url(r'^list/$', views.list, name='list'),  #一覧
    url(r'^test/$', views.test, name='test'),  #テスト
    url(r'^display/(?P<image_id>\d+)/$', views.display, name='display'),  #選択画像表示
    url(r'^add/$', views.MultiFileUpload, name='add'),  #登録
    url(r'^del/(?P<image_id>\d+)/$', views.Image_del, name='image_del'),  #登録
#    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
#    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除

)
