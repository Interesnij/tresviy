from django.conf.urls import url
from follows.views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', FollowsView.as_view(), name='follows'),
    url(r'^out/(?P<pk>\d+)/$', FollowingsView.as_view(), name='followings'),
    url(r'^add/(?P<pk>\d+)/$', FollowCreate.as_view(), name="create_follow"),
    url(r'^delete/(?P<pk>\d+)/$', FollowDelete.as_view(), name="delete_follow"),
    url(r'^add_member/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', CommunityFollowCreate.as_view(), name="create_community_follow"),
    url(r'^delete_member/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', CommunityFollowDelete.as_view(), name="delete_community_follow"),
]
