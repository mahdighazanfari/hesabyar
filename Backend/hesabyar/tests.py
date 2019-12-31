import json

import requests
from django.test import TestCase, Client

from hesabyar.models import User, Contact


class APITestCase(TestCase):
    @staticmethod
    def test_api() -> None:
        c = Client()
        User.objects.create_user('user1', 'lennon@thebeatles.com', 'pass', phone='09358888888').save()
        User.objects.create_user('user2', 'lggl@thebeatles.com', 'pass', phone='09358877888').save()
        assert json.loads(c.post('/login', {'user': 'user1', 'password': 'pass'}).content)['user'] == 1
        print('login ok')
        Contact(user=User.objects.get(pk=1), contact=User.objects.get(pk=2)).save()
        contacts = json.loads(c.post('/contact/get', {'user': 1}).content)
        assert contacts[0]['fields']['user'] == 1 and contacts[0]['fields']['contact'] == 2
        print('contacts ok')
        resp = json.loads(
            c.post('/transaction/new', {'user': 1, 'amount': 50, 'category': 1, 'members': [1, 2]}).content)
        assert resp['status'] == 'ok'
        print('new tran ok')
        resp = json.loads(c.post('/transaction/get', {'user': 1}).content)
        print(resp)
        resp = json.loads(
            c.post('/transaction/edit', {'transaction': 1, 'amount': 20, 'category': 2, 'members': [2]}).content)
        assert resp['status'] == 'ok'
        print('edit tran ok')
        resp = json.loads(c.post('/transaction/get', {'user': 1}).content)
        print(resp)
        resp = json.loads(c.post('/transaction/delete', {'transaction': 1}).content)
        assert resp['status'] == 'ok'
        print('delete tran ok')
        resp = json.loads(c.post('/transaction/get', {'user': 1}).content)
        print(resp)
