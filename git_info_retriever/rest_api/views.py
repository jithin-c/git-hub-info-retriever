from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from forms import UserSearchForm
from models import GitUser


class SearchUsersView(APIView):
    """
    Search and create users from git api.
    """

    def post(self, request, format=None):
        user_search_form = UserSearchForm(data=request.data)

        if user_search_form.is_valid():
            user_list = GitUser.call_git_search_api(request.data)
            GitUser.store_user_list(user_list)
            return Response(user_list, status=status.HTTP_201_CREATED)

        return Response(user_search_form.errors, status=status.HTTP_400_BAD_REQUEST)