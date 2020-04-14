from django import forms
from .models import Post, Comment

from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ('status','slug','author','publish')

class AdminPostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ('slug',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)