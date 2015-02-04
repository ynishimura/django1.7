# -*- coding: utf-8 -*-
from django import forms

CHOICES = (
        (0, '脳部位の体積算出'),
        (1, '画像処理'),
        (2, '処理をしない'),
        )
CHOICES_tag = (
        (0,'海馬の体積：Hippocampus'),
        (2,'帯状回の体積：Cingulum'),
        (3,'扁桃体の体積：Amygdala'),
        (4,'前頭葉の体積：Frontal_Lobe'),
        )

class ExampleForm(forms.Form):
    select_processing = forms.ChoiceField(choices=CHOICES, label='処理の選択',initial='実行したい処理を選択して下さい')
    choice_tag = forms.MultipleChoiceField(label='追加するタグ',choices=CHOICES_tag, widget=forms.CheckboxSelectMultiple)
    set_threshold0 = forms.IntegerField(label='海馬の体積の閾値の設定（単位：mm^3）',initial=3650)
    set_threshold2 = forms.IntegerField(label='帯状回の閾値の設定（単位：mm^3）',initial=5500)
    set_threshold3 = forms.IntegerField(label='扁桃体の閾値の設定（単位：mm^3）',initial=1248)
    set_threshold4 = forms.IntegerField(label='前頭葉の閾値の設定（単位：cm^3）',initial=550)
#    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
#    multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
#    multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
#    file_fied = forms.FileField()
#    password_field = forms.CharField(widget=forms.PasswordInput)
#    textarea = forms.CharField(widget=forms.Textarea)
#    boolean_field = forms.BooleanField()
