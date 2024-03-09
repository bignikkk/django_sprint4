from django.contrib.auth import get_user_model
from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

User = get_user_model()


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'pub_date', 'category', 'location']

    def disable_readonly_fields(self):
        self.fields['category'].disabled = True
        self.fields['location'].disabled = True


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
