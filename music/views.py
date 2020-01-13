from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render_to_response
from music.models import *


class AllMusicView(TemplateView):
    template_name="all_music.html"

    def get(self,request,*args,**kwargs):
        self.rus_simbols=SoundSymbol.objects.filter(type='RS')
        self.angl_simbols=SoundSymbol.objects.filter(type='AS')
        self.number_simbols=SoundSymbol.objects.filter(type='NS')
        self.all_music_count = SoundParsing.objects.only('release_year').count()
        return super(AllMusicView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(AllMusicView,self).get_context_data(**kwargs)
        context["rus_simbols"] = self.rus_simbols
        context["angl_simbols"] = self.angl_simbols
        context["number_simbols"] = self.number_simbols
        context["all_music_count"] = self.all_music_count
        return context


class AllTagsMusicView(TemplateView):
    template_name="music/tags_music.html"

    def get(self,request,*args,**kwargs):
        self.symbol=SoundSymbol.objects.get(pk=self.kwargs["pk"])
        self.tags=SoundTags.objects.filter(symbol=self.symbol)
        return super(AllTagsMusicView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(AllTagsMusicView,self).get_context_data(**kwargs)
        context["symbol"] = self.symbol
        context["tags"] = self.tags
        return context


class AllTagMusicView(TemplateView):
    template_name="music/tag_music.html"

    def get(self,request,*args,**kwargs):
        self.tag=SoundTags.objects.get(pk=self.kwargs["pk"])
        if request.user.is_authenticated:
            self.is_tag_playlist = request.user.is_tag_playlist(self.tag)
        return super(AllTagMusicView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(AllTagMusicView,self).get_context_data(**kwargs)
        context["tag"] = self.tag
        context["is_tag_playlist"] = self.is_tag_playlist
        return context


class AllSearchMusicView(View):
    template_name="search_music.html"
    def get(self,request,*args,**kwargs):
        client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
        if request.method == 'GET':
            q = request.GET.get('music_search')
            s_tracks = client.get('/tracks', q=q, license='cc-by-sa')
            response = render(request,'all_music.html',{'tracks_list':s_tracks,'q':q})
            return response
        return super(AllSearchMusicView,self).get(request,*args,**kwargs)
