from django import forms

def is_anagram(x, y):
    return sorted(x) == sorted(y)

class AnagramForm(forms.Form):
    test_value = forms.CharField(
        label='Your Name: ',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    test_anagram = forms.CharField(
        label='Test Anagram',
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    def clean(self):
        cleaned_data = super().clean()
        test_value = cleaned_data.get('test_value')
        test_anagram = cleaned_data.get('test_anagram')

        if test_value and test_anagram:
            if not is_anagram(test_value, test_anagram):
                raise forms.ValidationError('Not Anagrams!!!')
