from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Post, Comment
from .forms import AdminPostForm

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form = AdminPostForm
    list_filter = ('created', 'status')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
