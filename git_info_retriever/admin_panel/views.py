from datetime import datetime, timedelta
from django.views.generic.base import TemplateView

from rest_api.forms import UserSearchForm
from rest_api.models import GitUser, UserAPICallHistory


class AdminPanelView(TemplateView):
    """
    Admin panel view to view and filter users
    """
    template_name = "admin_panel.html"
    user_list = GitUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminPanelView, self).get_context_data(**kwargs)
        context['user_list'] = self.user_list

        user_reports = {}
        api_reports = {}

        current_time = datetime.now()
        user_reports['monthly'] = GitUser.objects.filter(created__gt=(current_time-timedelta(days=30))).count()
        user_reports['weekly'] = GitUser.objects.filter(created__gt=(current_time-timedelta(days=7))).count()
        user_reports['today'] = GitUser.objects.filter(created__day=current_time.day).count()

        api_reports['monthly'] = UserAPICallHistory.objects.filter(created__gt=(current_time-timedelta(days=30))).count()
        api_reports['weekly'] = UserAPICallHistory.objects.filter(created__gt=(current_time - timedelta(days=7))).count()
        api_reports['today'] = UserAPICallHistory.objects.filter(created__day=current_time.day).count()

        context['user_reports'] = user_reports
        context['api_reports'] = api_reports
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