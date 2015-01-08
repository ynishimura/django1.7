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
from misl_viewer.forms import ExampleForm

class testUploadFileForm(Form):
    file = FileField()

def test(request):

    return HttpResponse(u'test')
    #return render_to_response('misl_viewer/test.html',  # 使用するテンプレート
#                            {'form': form},       # テンプレートに渡すデータ
 #                           context_instance=RequestContext(request))  # その他標準のコンテキスト



def index(request):
    '''HOME'''
#    books = Book.objects.all().order_by('id')
    msg=''
    FILENAME=''
    name=''
    pngdir = '/root/webapp/django/dicom_viewer/dicom_web_viewer/static/png/'
    MultiFileUpload(request)

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

def Upload(request):
    '''アップロードページ'''
#    return HttpResponse(u'アップロードページ')
    form = ExampleForm()
    return render_to_response('misl_viewer/upload.html',
            {'form':form},
            context_instance=RequestContext(request))
def MultiFileUpload(request):
    '''複数ファイルアップロード'''
    filedir = r'/root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/'
    if request.method == 'POST':
        print request.POST
        print request.FILES
        for f in request.FILES.getlist('upload[]'):
            print f
            updir = filedir + str(f)
            destination = open(updir,'wb+')
            upfile = request.FILES['upload[]']
            for chunk in upfile.chunks():
                destination.write(chunk)
            destination.close()
