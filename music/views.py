import soundcloud
from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render_to_response
from django.http import JsonResponse


class AllMusicView(TemplateView):
    template_name="all_music.html"


class AllMusicListView(View):
    template_name="all_music_list.html"
    def get(self,request,*args,**kwargs):
        context = {}
        client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
        page_size = 100
        all_tracks = client.get('/tracks', genres='all', order='created_at', limit=page_size)
        context['request_user'] = request.user
        context['all_tracks'] = all_tracks
        return render_to_response('all_music_list.html', context)


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
