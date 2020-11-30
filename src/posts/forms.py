from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Post something...', 'class': 'form-style'}),
        }
