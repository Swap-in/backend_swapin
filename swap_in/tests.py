import unittest
from django.test import Client


class getNotificationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.access_token = 'cfd959c22925e12848651a77a84fcf71c1e4f9db'
        self.headers = {
           'HTTP_AUTHORIZATION': 'Token ' + self.access_token
        }

    def test_Get_Categories(self):

        response = self.client.get('/clothes/get_categories/', **self.headers)

        self.assertEqual(response.status_code, 200)
        
    def test_Get_Notifications_By_User(self):
        response = self.client.get('/clothes/notification_user/1/', **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_Get_Notification_By_Clothes(self):
        response = self.client.get('/clothes/notification_clothe/2/', **self.headers)

        self.assertEqual(response.status_code, 200)
       
    def test_Get_Search_Clothes(self):
        response = self.client.get('/clothes/search_clothes/2/1/', **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_Post_like(self):
        json = {
            "clothe_id": 2,
            "user_id": 1,
            "type_like": "SUPERLIKE"
        }
        response = self.client.post('/clothes/like/', json, **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_Post_notification(self):
        json = {
            "notification_id": 70
        }

        response = self.client.post('/clothes/notification_read/', json, **self.headers)

        self.assertEqual(response.status_code, 201)
