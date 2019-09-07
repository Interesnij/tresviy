from django.views.generic import ListView
from users.models import User
from connections.models import Communities


class CommunitiesView(ListView):
	template_name="connections.html"
	model=Communities

	def get(self,request,*args,**kwargs):
		self.user=User.objects.get(pk=self.kwargs["pk"])
		self.groups=Communities.objects.filter(target_connection__user=self.user)
		return super(CommunitiesView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunitiesView,self).get_context_data(**kwargs)
		context["groups"]=self.groups
		context['user'] = self.user
		return context
