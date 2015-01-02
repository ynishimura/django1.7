# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from misl_viewer import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dicom_web_viewer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^viewer/', include('misl_viewer.urls',namespace='misl_viewer')),
)
