from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter again !')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    #the above line is in order to catch bots from tampering the website
    def clean(self):
        clean_all_data = super().clean()
        email = clean_all_data['email']
        verify_email = clean_all_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Make Sure emails match !!")
