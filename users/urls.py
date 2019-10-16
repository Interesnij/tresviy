from django.conf.urls import url
from users.views import (
                            AllUsers,
                            UserItemView,
                            ProfileUserView,
                            UserGeneralChange,
                            UserAboutChange,
                            UserDesign,
                            PostUserView,
                            UserAvatarChange,
                            ProfileButtonReload,
                            fixed,
                            unfixed,
                        )

urlpatterns = [
    url(r'^all-users/$', AllUsers.as_view(), name='all_users'),
    url(r'^(?P<pk>\d+)/$', ProfileUserView.as_view(), name='user'),
    url(r'^item/(?P<pk>\d+)/$', UserItemView.as_view(), name='user_item'),
    url(r'^general/(?P<pk>[0-9]+)/$',
        UserGeneralChange.as_view(), name='user_general_form'),
    url(r'^list/(?P<pk>\d+)/$', PostUserView.as_view(), name="post_user_list"),
    url(r'^about/(?P<pk>[0-9]+)/$',
        UserAboutChange.as_view(), name='user_about_form'),
    url(r'^design/(?P<pk>\d+)/$', UserDesign.as_view(), name='user_design'),
    url(r'^fixed/(?P<uuid>[0-9a-f-]+)/$', fixed, name='fixed'),
    url(r'^unfixed/(?P<uuid>[0-9a-f-]+)/$', unfixed, name='unfixed'),
    url(r'^avatar/(?P<pk>[0-9]+)/$',
        UserAvatarChange.as_view(), name='user_avatar_form'),
    url(r'^profile_button/(?P<pk>[0-9]+)/$', ProfileButtonReload.as_view(), name='profile_button_reload'),
]
