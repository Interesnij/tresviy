import re
MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
from django.views.generic.base import TemplateView
from users.models import User
from posts.models import PostComment
from gallery.models import Album, Photo
from gallery.forms import PhotoDescriptionForm
from communities.models import Community
from common.template.photo import *
from django.http import Http404


class UserPhoto(TemplateView):
    """
    страница фото, не имеющего альбома для пользователя с разрещениями и без
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.photo = Photo.objects.get(uuid=self.kwargs["uuid"])
        self.photos = self.photo.creator.get_photos()
        if request.is_ajax():
            self.template_name = get_permission_user_photo(self.photo.creator, "u_photo/photo/", "photo.html", request.user)
        else:
            raise Http404

        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(UserPhoto,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserPhoto,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["next"] = self.photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["avatar"] = self.photo.is_avatar(self.request.user)
        context["user_form"] = PhotoDescriptionForm(instance=self.photo)
        return context


class UserAlbumPhoto(TemplateView):
    """
    страница отдельного фото в альбоме для пользователя с разрещениями и без
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.photo = Photo.objects.get(pk=self.kwargs["pk"])
        self.album = Album.objects.get(uuid=self.kwargs["album_uuid"])
        self.photos = self.photo.creator.get_photos_for_my_album(album_id=self.album.pk)
        if request.is_ajax():
            self.template_name = get_permission_user_photo(self.photo.creator, "u_photo/album_photo/", "photo.html", request.user)
        else:
            raise Http404

        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(UserAlbumPhoto,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserAlbumPhoto,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["album"] = self.album
        context["next"] = self.photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["avatar"] = self.photo.is_avatar(self.request.user)
        context["user_form"] = PhotoDescriptionForm(instance=self.photo)
        return context


class UserWallPhoto(TemplateView):
    """
    страница отдельного фото альбома пользователя "Фото со стены"
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.photo = Photo.objects.get(uuid=self.kwargs["uuid"])
        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.album = Album.objects.get(creator_id=self.user.pk, community=None, type=Album.WALL)
        self.photos = self.user.get_photos_for_album(album_id=self.album.pk)
        if request.is_ajax():
            self.template_name = get_permission_user_photo(self.photo.creator, "u_photo/wall_photo/", "photo.html", request.user)
        else:
            raise Http404
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(UserWallPhoto,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserWallPhoto,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["user_form"] = PhotoDescriptionForm(instance=self.photo)
        context["avatar"] = self.photo.is_avatar(self.request.user)
        context["next"] = self.photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["album"] = self.album
        return context


class UserDetailAvatar(TemplateView):
    """
    страница отдельного фото аватаров (альбом "Фото со страницы") пользователя с разрещениями и без
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.photo = Photo.objects.get(uuid=self.kwargs["uuid"])
        self.avatar_photos = self.photo.creator.get_avatar_photos()
        if request.is_ajax():
            self.template_name = get_permission_user_photo(self.photo.creator, "u_photo/avatar/", "photo.html", request.user)
        else:
            raise Http404
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(UserDetailAvatar,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserDetailAvatar,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["next"] = self.avatar_photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.avatar_photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["user_form"] = PhotoDescriptionForm(instance=self.photo)
        context["album"] = Album.objects.get(creator=self.photo.creator, type=Album.AVATAR, community=None)
        return context

class CommunityDetailAvatar(TemplateView):
    """
    страница отдельного фото альбома "Фото со страницы" сообщества с разрещениями и без
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.photo = Photo.objects.get(uuid=self.kwargs["uuid"])
        self.form_image = PhotoDescriptionForm(request.POST,instance=self.photo)
        self.avatar_photos = self.photo.community.get_avatar_photos()
        if request.is_ajax():
            self.template_name = get_permission_community_photo(self.photo.community, "c_photo/avatar/", "photo.html", request.user)
        else:
            raise Http404
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(CommunityDetailAvatar,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CommunityDetailAvatar,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["next"] = self.avatar_photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.avatar_photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["album"] = Album.objects.get(community=self.photo.community, type=Album.AVATAR)
        return context


class CommunityPhoto(TemplateView):
    """
    страница фото, не имеющего альбома для сообщества с разрещениями и без
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.photo = Photo.objects.get(uuid=self.kwargs["uuid"])
        self.photos = self.photo.community.get_photos()
        if request.is_ajax():
            self.template_name = get_permission_community_photo(self.photo.community, "c_photo/photo/", "photo.html", request.user)
        else:
            raise Http404
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(CommunityPhoto,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CommunityPhoto,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["next"] = self.photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["avatar"] = self.photo.is_avatar(self.request.user)
        return context


class CommunityAlbumPhoto(TemplateView):
    """
    страница отдельного фото в альбоме для пользователя с разрещениями и без
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.photo = Photo.objects.get(pk=self.kwargs["pk"])
        self.album=Album.objects.get(uuid=self.kwargs["album_uuid"])
        if request.is_ajax():
            self.template_name = get_permission_community_photo(self.album.community, "c_photo/album_photo/", "photo.html", request.user)
        else:
            raise Http404
        if request.user.is_administrator_of_community_with_name(self.album.community.name):
            self.photos = self.album.get_staff_photos()
        else:
            self.photos = self.album.get_photos()

        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(CommunityAlbumPhoto,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CommunityAlbumPhoto,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["album"] = self.album
        context["next"] = self.photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["avatar"] = self.photo.is_avatar(self.request.user)
        context["user_form"] = PhotoDescriptionForm(instance=self.photo)
        return context


class CommunityWallPhoto(TemplateView):
    """
    страница отдельного фото альбома сообщества "Фото со стены"
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.community = Community.objects.get(pk=self.kwargs["pk"])
        self.photo = Photo.objects.get(uuid=self.kwargs["uuid"])
        self.album = Album.objects.get(community=self.community, type=Album.WALL)
        self.photos = self.community.get_photos_for_album(album_id=self.album.pk)
        if request.is_ajax():
            self.template_name = get_permission_community_photo(self.community, "c_photo/wall_photo/", "photo.html", request.user)
        else:
            raise Http404
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(CommunityWallPhoto,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CommunityWallPhoto,self).get_context_data(**kwargs)
        context["object"] = self.photo
        context["user_form"] = PhotoDescriptionForm(instance=self.photo)
        context["avatar"] = self.photo.is_avatar(self.request.user)
        context["next"] = self.photos.filter(pk__gt=self.photo.pk).order_by('pk').first()
        context["prev"] = self.photos.filter(pk__lt=self.photo.pk).order_by('-pk').first()
        context["album"] = self.album
        return context
