from django.conf.urls import url
from managers.view.audio import (
                                AudioAdminCreate,
                                AudioAdminDelete,
                                AudioModerCreate,
                                AudioModerDelete,
                                AudioEditorCreate,
                                AudioEditorDelete,

                                AudioWorkerAdminCreate,
                                AudioWorkerAdminDelete,
                                AudioWorkerModerCreate,
                                AudioWorkerModerDelete,
                                AudioWorkerEditorCreate,
                                AudioWorkerEditorDelete
                            )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add_admin/(?P<pk>\d+)/$', login_required(AudioAdminCreate.as_view())),
    url(r'^delete_admin/(?P<pk>\d+)/$', login_required(AudioAdminDelete.as_view())),
    url(r'^add_moderator/(?P<pk>\d+)/$', login_required(AudioModerCreate.as_view())),
    url(r'^delete_moderator/(?P<pk>\d+)/$', login_required(AudioModerDelete.as_view())),
    url(r'^add_editor/(?P<pk>\d+)/$', login_required(AudioEditorCreate.as_view())),
    url(r'^delete_editor/(?P<pk>\d+)/$', login_required(AudioEditorDelete.as_view())),

    url(r'^add_worker_admin/(?P<pk>\d+)/$', login_required(AudioWorkerAdminCreate.as_view())),
    url(r'^delete_worker_admin/(?P<pk>\d+)/$', login_required(AudioWorkerAdminDelete.as_view())),
    url(r'^add_worker_moderator/(?P<pk>\d+)/$', login_required(AudioWorkerModerCreate.as_view())),
    url(r'^delete_worker_moderator/(?P<pk>\d+)/$', login_required(AudioWorkerModerDelete.as_view())),
    url(r'^add_worker_editor/(?P<pk>\d+)/$', login_required(AudioWorkerEditorCreate.as_view())),
    url(r'^delete_worker_editor/(?P<pk>\d+)/$', login_required(AudioWorkerEditorDelete.as_view()))
]
