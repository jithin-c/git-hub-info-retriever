from django.conf.urls import url
import views

urlpatterns = [
    url(r'^search-users/', views.SearchUsersView.as_view(), name='search_users'),
]
