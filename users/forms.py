from django import forms
from users.model.profile import UserProfile
from users.model.settings import UserPostNotifications


class InfoUserForm(forms.ModelForm):
    first_name = forms.CharField(required=False,max_length=256,label='Имя')
    last_name = forms.CharField(required=False,max_length=256,label='Фамилия')

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','sity')


class SettingsNotifyForm(forms.ModelForm):

    class Meta:
        model = UserPostNotifications
        fields = (
            'comment',
            'comment_reply',
            'repost',
            'like',
            'dislike',
            'comment_like',
            'comment_dislike',
            'comment_reply_like',
            'comment_reply_dislike',
        )
