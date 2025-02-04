from django import forms

class FormEnterCnt(forms.Form):
    name_file = forms.FilePathField(path='D:\MyExamplePython\pythonProject1\count_word\media',label="выберите файл")
    word = forms.CharField(max_length=100,label='слово для расчета')
