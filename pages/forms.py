from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your email address', required=False)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)