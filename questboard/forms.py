from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(max_length=20, label='Name:')
    description = forms.CharField(widget=forms.Textarea, label='Description:')
    rstars = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)], label='Required Stars:')