from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ExampleForm(forms.Form):
    mydate_field = forms.DateField(widget=DateInput) # instanciate the DateInput class defined above


class ExampleModelForm(forms.Form):

    class Meta:
        widgets = {'mydate_field': DateInput()}  # instanciate the DateInput class defined above