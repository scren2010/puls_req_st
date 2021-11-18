from django.test import TestCase
from .models import UserRequestResult, UserRequest
from django.urls import reverse


# Create your tests here.
class UserRequestTestClass(TestCase):

    def setUp(self):
        user_link = UserRequest.objects.create(user_link='https://github.com/DJWOMS/djangochannel/pulls')
        user_link.save()

    def test_user_link_label(self):
        user_link = UserRequest.objects.get(id=1)
        field_label = user_link._meta.get_field('user_link').verbose_name
        self.assertEquals(field_label, 'Ссылка на публичный репозиторий')

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home_view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'pull_req_app/home.html')

        self.assertFalse('is_paginated' in resp.context)


class UserRequestResultTestClass(TestCase):
    def setUp(self):
        user_link = UserRequest.objects.create(user_link='https://github.com/DJWOMS/djangochan1nel/pulls')
        user_link.save()
        pull_request_result = UserRequestResult.objects.create(user_link=user_link, pull_request='Update das dasd a',
                                                               pull_request_link='https://github.com/DJWOMS/djan11gochannel/pulls/1',
                                                               )
        pull_request_result.save()

    def test_pull_request_result_label(self):
        pull_request_result = UserRequestResult.objects.first()
        pull_request_reviewers_label = pull_request_result._meta.get_field('pull_request_reviewers').verbose_name
        pull_request_assignees_label = pull_request_result._meta.get_field('pull_request_assignees').verbose_name
        self.assertEquals(pull_request_reviewers_label, 'Reviewers (usernames)')
        self.assertEquals(pull_request_assignees_label, 'Assignees (usernames)')

    def test_pull_request_reviewers_max_length(self):
        pull_request_result = UserRequestResult.objects.first()
        max_length1 = pull_request_result._meta.get_field('pull_request_reviewers').max_length
        max_length2 = pull_request_result._meta.get_field('pull_request_assignees').max_length
        self.assertEquals(max_length1, 100)
        self.assertEquals(max_length2, 100)

    def test_req_create(self):
        pull_request_result = UserRequestResult.objects.first()
        self.assertEquals(pull_request_result.pull_request_link, 'https://github.com/DJWOMS/djan11gochannel/pulls/1')
        self.assertEquals(pull_request_result.pull_request_link, 'https://github.com/DJWOMS/djan11gochannel/pulls/1')
