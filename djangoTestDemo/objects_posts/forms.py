from djangoTestDemo.objects_posts.models import Post, Object
from django import forms


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('object', 'found')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('object',)


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"
