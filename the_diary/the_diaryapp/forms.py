from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):

    class Meta:  #adds extra info to a class
        model = Entry
        fields = ('text',)

    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'textarea','placeholder':'whatg\'s on your mind?'})