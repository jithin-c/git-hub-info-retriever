from django.views.generic.base import TemplateView

from rest_api.forms import UserSearchForm
from rest_api.models import GitUser

class AdminPanelView(TemplateView):
    """
    Admin panel view to view and filter users
    """
    template_name = "admin_panel.html"
    user_list = GitUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminPanelView, self).get_context_data(**kwargs)
        context['user_list'] = self.user_list
        return context

    def post(self, request, *args, **kwargs):
        user_search_form = UserSearchForm(request.POST)
        if user_search_form.is_valid():
            filterby = {}
            for key,val in user_search_form.cleaned_data.iteritems():
                if val:
                    filterby[key] = val
            self.user_list = GitUser.objects.filter(**filterby)
        return self.get(request, *args, **kwargs)