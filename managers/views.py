from django.views.generic.base import TemplateView


class ManagersView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            self.template_name = "managers.html"
        return super(ManagersView,self).get(request,*args,**kwargs)


class TermsView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            self.template_name = "terms/terms.html"
        else:
            self.template_name = "terms/anon_terms.html"
        return super(TermsView,self).get(request,*args,**kwargs)


class PolicyView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            self.template_name = "policy/policy.html"
        else:
            self.template_name = "policy/anon_policy.html"
        return super(PolicyView,self).get(request,*args,**kwargs)


class LicenceView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            self.template_name = "licence/licence.html"
        else:
            self.template_name = "licence/anon_licence.html"
        return super(LicenceView,self).get(request,*args,**kwargs)
