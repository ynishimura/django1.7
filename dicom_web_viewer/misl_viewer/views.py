# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
#file upload#
from django.forms import *
from misl_viewer.forms import ExampleForm
#model#
from misl_viewer.models import Image
#system cmd#
import os

class testUploadFileForm(Form):
    file = FileField()

def test(request):
    return HttpResponse(u'test')

def index(request):
    '''HOME'''
    msg=''
    FILENAME=''
    name=''
    pngdir = '/root/webapp/django/dicom_viewer/dicom_web_viewer/static/png/'
    MultiFileUpload(request)

    # #-- upload method --#
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         updir = r'/root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/' + form.cleaned_data['name']
    #         destination = open(updir,'wb+')
    #         upfile = request.FILES['file']
    #         for chunk in upfile.chunks():
    #             destination.write(chunk)
    #         destination.close()
    #
    #         # #set#
    #         FILENAME = form.cleaned_data['name']
    #         name , ext = os.path.splitext(FILENAME)
    #
    #         #-- dcm convert --#
    #         cmd2 = "dcm2pnm --write-png "+ filedir + name + ".dcm " + pngdir + name + ".png"
    #         os.system(cmd2)
    #
    # else:
    #     form = UploadFileForm()

    #-- dcm convert --#
    #cmd1 = "dcmdjpeg /root/webapp/django/dicom_viewer/dicom_web_viewer/static/file/" + name + ".dcm /root/webapp/django/dicom_viewer/dicom_web_viewer/static/jpg/" + name + ".dcm"

    return render_to_response('misl_viewer/index.html',  # 使用するテンプレート
                              context_instance=RequestContext(request))  # その他標準のコンテキスト


class UploadFileForm(Form):
	#name = CharField(max_length = 50)
	file = FileField()

def list(request):
    '''画像一覧'''
    images = Image.objects.all()
    print Image.objects.all().order_by('id')
    return render_to_response('misl_viewer/list.html',  # 使用するテンプレート
                              {'images': images},       # テンプレートに渡すデータ
                              context_instance=RequestContext(request))  # その他標準のコンテキスト

def display(request, image_id):
    '''選択画像表示'''
    image_display = get_object_or_404(Image, pk=image_id)
    return render_to_response('misl_viewer/display.html',  # 使用するテンプレート
                              {'images': image_display},       # テンプレートに渡すデータ
                              context_instance=RequestContext(request))  # その他標準のコンテキスト


def Image_del(request,image_id):
    '''画像の削除'''
    image = get_object_or_404(Image, pk=image_id)
    image.delete()
    return redirect('misl_viewer:list')

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
#        print request.POST['select_processing']
 #       print request.POST['set_threshold']
#        print request.FILES
        for f in request.FILES.getlist('upload[]'):
            print f
            updir = filedir + str(f)
            #db save
            i = Image(file_name= str(f))
            #i = Image(file_name= str(f),set_proc= request.POST['select_processing'],set_threshold=request.POST['set_threshold'])
            i.save()
            #
            destination = open(updir,'wb+')
            upfile = request.FILES['upload[]']
            for chunk in upfile.chunks():
                destination.write(chunk)
            destination.close()
        os.system("ssh debian python /root/dicom_image/dicom_addtag.py")
        os.system("ssh debian python /root/dicom_image/dicom_convert.py")
    return redirect('/viewer/list')
