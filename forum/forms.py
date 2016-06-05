
# make sure this is at the top if it isn't already
from django import forms

# our new form
class ThreadForm(forms.Form):
    title = forms.CharField(required=True, label='',
    	widget=forms.TextInput(attrs={'placeholder': 'Enter Title Here'}))
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
                attrs={'placeholder': 'Enter Description Here'}),
        label=''

    )

class CommentForm(forms.Form):
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
                attrs={'placeholder': 'Enter Comment Here'}),
        label=''

    )	
