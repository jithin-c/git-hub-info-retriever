import json
from django.db import models
import requests

GIT_API_URL = "https://api.github.com/search/users?"


class GitUser(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    login = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250, blank=True, null=True)
    avatar_url = models.CharField(max_length=1000, blank=True, default='')
    email = models.EmailField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    @staticmethod
    def call_git_search_api(params_dict):
        query_string = "q="
        for key, val in params_dict.iteritems():
            if val:
                query_string = query_string + val + " in:" + key
        query_string += " type:user"

        url = GIT_API_URL + query_string
        response = requests.get(url)
        user_list = {}
        if response.status_code == 200:
            user_list = json.loads(response.content)
        return user_list

    @classmethod
    def store_user_list(cls, user_list):
        users = user_list.get('items', [])

        for user in users:
            user_id = user.get('id')
            if cls.objects.filter(id=user_id).exists():
                user_obj = cls.objects.get(id = user_id)
            else:
                user_obj = cls()

            user_obj.id = user_id
            user_obj.login = user.get('login')
            user_obj.avatar_url = user.get('avatar_url')

            user_url = user.get('url')

            user_fullname = ""
            user_email = ""
            if user_url:
                response = requests.get(user_url)
                if response.status_code == 200:
                    user_details = json.loads(response.content)
                    user_fullname = user_details.get('name')
                    user_email = user_details.get('email')

            user_obj.fullname = user_fullname
            user_obj.email = user_email
            user_obj.save()