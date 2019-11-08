from django.views.generic import ListView
from communities.models import Community, CommunityMembership
from generic.mixins import CommunityMemdersMixin



class CommunitiesView(ListView):
	template_name="communities.html"
	model=Community
	paginate_by=15

	def get_queryset(self):
		self.user=User.objects.get(pk=self.kwargs["pk"])
		groups=Community.objects.filter(memberships__user__id=self.user.pk)
		return groups


class CommunityMembersView(ListView, CommunityMemdersMixin):
	template_name="members.html"
	model=Community
	paginate_by=15

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		return super(CommunityMembersView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityMembersView,self).get_context_data(**kwargs)
		context["community"]=self.community
		return context

	def get_queryset(self):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		membersheeps=CommunityMembership.objects.filter(community__id=self.community.pk)
		return membersheeps


class AllCommunities(ListView):
	template_name="all_communities.html"
	model=Community
	paginate_by=15

	def get_queryset(self):
		groups=Community.objects.all()
		return groups
