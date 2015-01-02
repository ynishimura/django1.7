# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
#file upload#
from django.forms import *
#model#
from misl_viewer.models import Upload
#system cmd#
import os

def test(request):

    msg=''
    FILENAME=''
    name=''
    filedir = '/root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/'
    pngdir = '/root/webapp/django/dicom_viewer/dicom_web_viewer/static/png/'
    #-- upload method --#
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        print form
        if form.is_valid():
            print form.cleaned_data
            #
            # updir = r'/root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/' + form.cleaned_data['name']
            # destination = open(updir,'wb+')
            # upfile = request.FILES['file']
            # for chunk in upfile.chunks():
            #     destination.write(chunk)
            # destination.close()
            #
            # # #set#
            # FILENAME = form.cleaned_data['name']
            # name , ext = os.path.splitext(FILENAME)
            #
            # #-- dcm convert --#
            # cmd2 = "dcm2pnm --write-png "+ filedir + name + ".dcm " + pngdir + name + ".png"
            # os.system(cmd2)

    else:
        form = UploadFileForm()

    #return HttpResponse(u'test')
    return render_to_response('misl_viewer/test.html',  # 使用するテンプレート
                            {'form': form},       # テンプレートに渡すデータ
                            context_instance=RequestContext(request))  # その他標準のコンテキスト



def index(request):
    '''HOME'''
#    return HttpResponse(u'home')
#    books = Book.objects.all().order_by('id')
    msg=''
    FILENAME=''
    name=''
    filedir = '/root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/'
    pngdir = '/root/webapp/django/dicom_viewer/dicom_web_viewer/static/png/'
    #-- upload method --#
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            updir = r'/root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/' + form.cleaned_data['name']
            destination = open(updir,'wb+')
            upfile = request.FILES['file']
            for chunk in upfile.chunks():
                destination.write(chunk)
            destination.close()

            # #set#
            FILENAME = form.cleaned_data['name']
            name , ext = os.path.splitext(FILENAME)

            #-- dcm convert --#
            cmd2 = "dcm2pnm --write-png "+ filedir + name + ".dcm " + pngdir + name + ".png"
            os.system(cmd2)

    else:
        form = UploadFileForm()

    #-- dcm convert --#
    #cmd1 = "dcmdjpeg /root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/" + name + ".dcm /root/webapp/django/dicom_viewer/dicom_web_viewer/static/jpg/" + name + ".dcm"

    return render_to_response('misl_viewer/index.html',  # 使用するテンプレート
                              {'form': form},       # テンプレートに渡すデータ
                              context_instance=RequestContext(request))  # その他標準のコンテキスト


class UploadFileForm(Form):
	#name = CharField(max_length = 50)
	file = FileField()

def list(request):
    '''画像一覧'''
    return HttpResponse(u'一覧')
#    books = Book.objects.all().order_by('id')
#    return render_to_response('misl_viewer/index.html',  # 使用するテンプレート
#                              {'books': books},       # テンプレートに渡すデータ
#                              context_instance=RequestContext(request))  # その他標準のコンテキスト


def upload(request):
    '''画像アップロード'''
    return HttpResponse(u'アップロード')
