from video.models import VideoAlbum, Video
from django import forms


class AlbumForm(forms.ModelForm):

	class Meta:
		model = VideoAlbum
		fields = ['title', 'is_public']


class VideoForm(forms.ModelForm):
	description = forms.CharField( label="", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))
	category = forms.CharField( label="", required=False, widget=forms.Select(attrs={'class': 'form-control'}))
	class Meta:
		model = Video
		fields = ['title', 'description', 'is_public', 'image', 'category', "tag" , 'album', 'is_child', 'comments_enabled', 'uri']
