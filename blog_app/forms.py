from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My Post Title'}),
            'category' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. music'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My Post Title'}),
            'category' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. music'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }