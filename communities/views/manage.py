from django.views.generic import ListView
from communities.models import *
from communities.model.settings import *
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from communities.forms import *
from users.models import User
from follows.models import CommunityFollow
from datetime import datetime, timedelta


class CommunityGeneralChange(TemplateView):
	template_name = None
	form=None

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=GeneralCommunityForm(instance=self.community)
		self.template_name = self.community.get_manage_template(folder="manage/", template="general.html", request=request)
		return super(CommunityGeneralChange,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityGeneralChange,self).get_context_data(**kwargs)
		context["form"]=self.form
		context["community"]=self.community
		return context

	def post(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=GeneralCommunityForm(request.POST, instance=self.community)
		if self.form.is_valid() and request.is_ajax() and request.user.is_administrator_of_community_with_name(self.community.name):
			self.form.save()
			return HttpResponse('!')
		else:
			return HttpResponseBadRequest()
		return super(CommunityGeneralChange,self).post(request,*args,**kwargs)


class CommunityAvatarChange(TemplateView):
	template_name = None
	form=None

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=AvatarCommunityForm()
		self.template_name = self.community.get_manage_template(folder="manage/", template="avatar.html", request=request)
		return super(CommunityAvatarChange,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityAvatarChange,self).get_context_data(**kwargs)
		context["community"]=self.community
		context["form"]=self.form
		return context

	def post(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=AvatarCommunityForm(request.POST,request.FILES, instance=self.community)
		if self.form.is_valid():
			self.form.save(commit=False)

			if request.is_ajax():
				return HttpResponse ('!')
		return super(CommunityAvatarChange,self).post(request,*args,**kwargs)


class CommunityCoverChange(TemplateView):
	template_name = None
	form=None

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=CoverCommunityForm()
		self.template_name = self.community.get_manage_template(folder="manage/", template="cover.html", request=request)
		return super(CommunityCoverChange,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityCoverChange,self).get_context_data(**kwargs)
		context["community"]=self.community
		context["form"]=self.form
		return context

	def post(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=CoverCommunityForm(request.POST,request.FILES, instance=self.community)
		if self.form.is_valid():
			self.form.save()
			if request.is_ajax():
				return HttpResponse ('!')
		return super(CommunityCoverChange,self).post(request,*args,**kwargs)


class CommunityCatChange(TemplateView):
	template_name = "manage/category.html"
	form=None
	categories = CommunityCategory.objects.only("id")

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=CatCommunityForm()
		return super(CommunityCatChange,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityCatChange,self).get_context_data(**kwargs)
		context["form"]=self.form
		context["community"]=self.community
		context["categories"]=self.categories
		return context

	def post(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=CatCommunityForm(request.POST, instance=self.community)
		if self.form.is_valid() and request.user.is_administrator_of_community_with_name(self.community.name):
			self.form.save()
			if request.is_ajax():
				return HttpResponse ('!')
		return super(CommunityCatChange,self).post(request,*args,**kwargs)


class CommunityNotifyView(TemplateView):
	template_name = None
	form=None
	notify_settings=None

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=CommunityNotifyForm()
		self.template_name = self.community.get_manage_template(folder="manage/", template="notifications_settings.html", request=request)
		try:
			self.notify_settings=CommunityNotificationsSettings.objects.get(community=self.community)
		except:
			self.notify_settings=CommunityNotificationsSettings.objects.create(community=self.community)
		return super(CommunityNotifyView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityNotifyView,self).get_context_data(**kwargs)
		context["form"]=self.form
		context["notify_settings"]=self.notify_settings
		context["community"]=self.community
		return context

	def post(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.notify_settings=CommunityNotificationsSettings.objects.get(community=self.community)
		self.form=CommunityNotifyForm(request.POST)
		if self.form.is_valid() and request.user.is_administrator_of_community_with_name(self.community.name):
			self.form.save()
			if request.is_ajax():
				return HttpResponse ('!')
		return super(CommunityNotifyView,self).post(request,*args,**kwargs)


class CommunityPrivateView(TemplateView):
	template_name = None
	form=None
	private_settings=None

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=CommunityPrivateForm()
		self.template_name = self.community.get_manage_template(folder="manage/", template="private_settings.html", request=request)
		try:
			self.private_settings=CommunityPrivateSettings.objects.get(community=self.community)
		except:
			self.private_settings=CommunityPrivateSettings.objects.create(community=self.community)
		return super(CommunityPrivateView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityPrivateView,self).get_context_data(**kwargs)
		context["form"]=self.form
		context["community"]=self.community
		context["private_settings"]=self.private_settings
		return context

	def post(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.form=CommunityPrivateForm(request.POST,instance=self.private_settings)
		if self.form.is_valid() and request.user.is_administrator_of_community_with_name(self.community.name):
			self.form.save()
			if request.is_ajax():
				return HttpResponse ('!')
		return super(CommunityPrivateView,self).post(request,*args,**kwargs)


class CommunityAdminView(ListView):
	template_name = None
	model = User
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_manage_template(folder="manage/", template="admins.html", request=request)
		return super(CommunityAdminView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityAdminView,self).get_context_data(**kwargs)
		context["community"] = self.community
		return context

	def get_queryset(self):
		admins = self.community.get_community_with_name_administrators(self.community.name)
		return admins


class CommunityEditorsView(ListView):
	template_name = None
	model = User
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_manage_template(folder="manage/", template="editors.html", request=request)
		return super(CommunityEditorsView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityEditorsView,self).get_context_data(**kwargs)
		context["community"] = self.community
		return context

	def get_queryset(self):
		admins = self.community.get_community_with_name_editors(self.community.name)
		return admins


class CommunityAdvertisersView(ListView):
	template_name = None
	model = User
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_manage_template(folder="manage/", template="advertisers.html", request=request)
		return super(CommunityAdvertisersView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityAdvertisersView,self).get_context_data(**kwargs)
		context["community"] = self.community
		return context

	def get_queryset(self):
		advertisers = self.community.get_community_with_name_advertisers(self.community.name)
		return advertisers


class CommunityModersView(ListView):
	template_name="manage/moders.html"
	model=User
	paginate_by=30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_manage_template(folder="manage/", template="moders.html", request=request)
		return super(CommunityModersView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityModersView,self).get_context_data(**kwargs)
		context["community"]=self.community
		return context

	def get_queryset(self):
		moders=self.community.get_community_with_name_moderators(self.community.name)
		return moders


class CommunityBlackListView(ListView):
	template_name="manage/black_list.html"
	model=User
	paginate_by=30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_moders_template(folder="manage/", template="moders.html", request=request)
		return super(CommunityBlackListView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunityBlackListView,self).get_context_data(**kwargs)
		context["community"]=self.community
		return context

	def get_queryset(self):
		black_list=self.community.get_community_with_name_banned_users(self.community.name)
		return black_list


class CommunityFollowsView(ListView):
	template_name = None
	model = CommunityFollow
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_manage_template(folder="manage/", template="follows.html", request=request)
		return super(CommunityFollowsView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityFollowsView,self).get_context_data(**kwargs)
		context["community"] = self.community
		return context

	def get_queryset(self):
		follows = CommunityFollow.get_community_with_name_follows(self.community.name)
		return follows


class CommunityMemberManageView(ListView):
	template_name = None
	model = Community
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.administrators = Community.get_community_with_name_administrators(self.community)
		self.moderators = Community.get_community_with_name_moderators(self.community)
		self.editors = Community.get_community_with_name_editors(self.community)
		self.advertisers = Community.get_community_with_name_advertisers(self.community)
		self.template_name = self.community.get_manage_template(folder="manage/", template="members.html", request=request)
		return super(CommunityMemberManageView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityMemberManageView,self).get_context_data(**kwargs)
		context["community"] = self.community
		context["administrators"] = self.administrators
		context["moderators"] = self.moderators
		context["editors"] = self.editors
		context["advertisers"] = self.advertisers
		return context

	def get_queryset(self):
		membersheeps = self.community.get_community_with_name_members(self.community.name)
		return membersheeps


class CommunityStaffWindow(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		self.administrator = self.user.is_administrator_of_community_with_name(self.community)
		self.moderator = self.user.is_moderator_of_community_with_name(self.community)
		self.editor = self.user.is_editor_of_community_with_name(self.community)
		self.advertiser = self.user.is_advertiser_of_community_with_name(self.community)
		self.template_name = self.community.get_manage_template(folder="manage/", template="staff_window.html", request=request)
		return super(CommunityStaffWindow,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityStaffWindow,self).get_context_data(**kwargs)
		context["community"] = self.community
		context["user"] = self.user
		context["administrator"] = self.administrator
		context["moderator"] = self.moderator
		context["editor"] = self.editor
		context["advertiser"] = self.advertiser
		return context


class CommunityStateCoberturaMonth(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		from stst.models import CommunityNumbers

		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_manage_template(folder="manage/", template="stat_cobertura_month.html", request=request)
		self.months = [i.month for i in CommunityNumbers.objects.values_list('created', flat=True)]
		self.today_query = CommunityNumbers.objects.filter(community=self.community.pk, created__month=self.months[0]).distinct().values('platform')
		try:
			self.prev_month = self.months[1]
			self.prev_count = CommunityNumbers.objects.filter(community=self.community.pk, created__month=self.months[1]).distinct().values('platform').count()
		except:
			self.prev_month = None
			self.prev_count = None
		try:
			self.prev2_month = self.months[2]
			self.prev2_count = CommunityNumbers.objects.filter(community=self.community.pk, created__month=self.months[2]).distinct().values('platform').count()
		except:
			self.prev2_month = None
			self.prev2_count = None
		try:
			self.prev3_month = self.months[3]
			self.prev3_count = CommunityNumbers.objects.filter(community=self.community.pk, created__month=self.months[3]).distinct().values('platform').count()
		except:
			self.prev3_count = None
			self.prev3_month = None
		try:
			self.prev4_month = self.months[4]
			self.prev4_count = CommunityNumbers.objects.filter(community=self.community.pk, created__month=self.months[4]).distinct().values('platform').count()
		except:
			self.prev4_count = None
			self.prev4_month = None

		if self.today_query:
			self.phone_count = self.today_query.filter(platform=1)
			self.comp_count = self.today_query.filter(platform=0)
			self.phone = len(self.phone_count)/len(self.today_query)*100
			self.comp = len(self.comp_count)/len(self.today_query)*100
		return super(CommunityStateCoberturaMonth,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityStateCoberturaMonth,self).get_context_data(**kwargs)
		context["community"] = self.community
		context["phone"] = self.phone or None
		context["comp"] = self.comp or None
		context["month"] = self.months[0]
		context["prev_month"] = self.prev_month
		context["prev2_month"] = self.prev2_month
		context["prev3_month"] = self.prev3_month
		context["prev4_month"] = self.prev4_month
		context["today_count"] =  len(self.today_query)
		context["prev_count"] =  self.prev_count
		context["prev2_count"] =  self.prev2_count
		context["prev3_count"] =  self.prev3_count
		context["prev4_count"] =  lself.prev4_count
		return context
