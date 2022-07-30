from django import forms


class MyfileUploadForm(forms.Form):
    uploadfiles = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))