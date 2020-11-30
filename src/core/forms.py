from .models import Post
from django import forms

class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_active', 'image')

    def save(self, user, *args, **kwargs):
        return super(*args, **kwargs)