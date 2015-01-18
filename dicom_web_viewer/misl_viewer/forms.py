# -*- coding: utf-8 -*-
from django import forms

CHOICES = (
        (0, '脳部位の体積算出'), 
        (1, '画像処理'), 
        (2, '処理をしない'),
        )
CHOICES_tag = (
        (0,'海馬の体積'),
        (1,'小脳の体積'),
        (0,'すべて追加'),
        )

class ExampleForm(forms.Form):
    select_processing = forms.ChoiceField(choices=CHOICES, label='処理の選択',initial='行いたい処理を選択して下さい')
    choice_tag = forms.MultipleChoiceField(label='DICOMタグに追加する項目',choices=CHOICES_tag, widget=forms.CheckboxSelectMultiple)
    set_threshold = forms.IntegerField(label='閾値の設定',initial=0)
#    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
#    multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
#    multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
#    file_fied = forms.FileField()
#    password_field = forms.CharField(widget=forms.PasswordInput)
#    textarea = forms.CharField(widget=forms.Textarea)
#    boolean_field = forms.BooleanField()

