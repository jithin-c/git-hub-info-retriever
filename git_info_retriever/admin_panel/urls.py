from django.conf.urls import url
import views

urlpatterns = [
    url(r'^', views.AdminPanelView.as_view(), name='search_users'),
]
