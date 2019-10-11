from posts.models import Post, PostComment2
from django import forms


class PostCommentForm(forms.ModelForm):

	class Meta:
		model = PostComment2
		fields = ['text']

class PostRepostForm(forms.Form):
    repost_comment = forms.CharField(widget=forms.Textarea)

class PostUserForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['text']
