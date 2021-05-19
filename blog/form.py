from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    # forms.TextInput(attrs={'placeholder': 'Your message goes here...'})
    # widget = {
    #     'labels': ['Name', 'Message']
    # }