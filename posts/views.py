from django.views.generic.base import TemplateView
from users.models import User
from django.template.loader import render_to_string
from posts.models import Post
from posts.forms import PostUserForm, PostCommunityForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View


class PostsView(TemplateView):
    template_name="posts.html"


class PostDetailView(TemplateView):
    model=Post
    template_name="post.html"

    def get(self,request,*args,**kwargs):
        self.post = Post.objects.get(uuid=self.kwargs["uuid"])
        self.post.views += 1
        self.post.save()
        return super(PostDetailView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostDetailView,self).get_context_data(**kwargs)
        context["object"]=self.post
        return context


class PostUserCreate(View):
    form_post=None
    success_url="/"

    def get(self,request,*args,**kwargs):
        self.form_post=PostUserForm(initial={"creator":request.user})
        return super(PostUserCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostUserCreate,self).get_context_data(**kwargs)
        context["form_post"]=self.form_post
        return context

    def post(self,request,*args,**kwargs):
        self.form_post=PostUserForm(request.POST, request.FILES)
        if self.form_post.is_valid():
            new_post=self.form_post.save(commit=False)
            new_post.creator=self.request.user
            new_post=self.form_post.save()

            if request.is_ajax() :
                html = render_to_string('new_post.html',{'object': new_post,'request': request})
                return HttpResponse(html)
        else:
            return HttpResponseBadRequest()


class PostCommunityCreate(View):
    form_post=None
    success_url="/"

    def get(self,request,*args,**kwargs):
        self.form_post=PostCommunityForm(initial={"creator":request.user,'community':request.POST.get('community'))
        return super(PostCommunityCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostCommunityCreate,self).get_context_data(**kwargs)
        context["form_post"]=self.form_post
        return context

    def post(self,request,*args,**kwargs):
        self.form_post=PostCommunityForm(request.POST, request.FILES)
        if self.form_post.is_valid():
            new_post=self.form_post.save(commit=False)
            new_post.creator=self.request.user
            new_post.community=request.POST.get('community')
            new_post=self.form_post.save()

            if request.is_ajax() :
                html = render_to_string('new_post.html',{'object': new_post,'request': request})
                return HttpResponse(html)
        else:
            return HttpResponseBadRequest()
