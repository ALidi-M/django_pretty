from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['name','email','purpose','message']

        # widgets = {
        #     'name':forms.TextInput(attrs= {'class':'input','placeholder':'your name here'}),
        #     'email':forms.EmailInput(attrs= {'class':'input','placeholder':'@example.com'}),
        #     'message':forms.Textarea(attrs={'class': 'textarea','rows': 10,'placeholder':'Enter your message'})
        # }