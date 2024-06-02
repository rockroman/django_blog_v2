from .models import Comment, Post
from django import forms
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    content = RichTextField()
    class Meta:
        model = Post
        fields = ("title", "content", "featured_image")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
