""" Test cases """
# Django
from django.test import TestCase, Client
from rest_framework.authtoken.models import Token

# Models
from swap_in.users.models import (
    User,
    Country
)
from swap_in.clothes.models import (
    Clothes,
    category,
    like,
    Match
)

class SwapinTestCasesSetUp(TestCase):
    """ Swapin model test case. """
    def setUp(self):
        self.country = Country.objects.create(
            country_code="COL",
            country_name="COLOMBIA"
        )

        self.username = User.objects.create(
            username="Test_user",
            first_name="Test",
            last_name="User",
            password="admin1234",
            email="test_email@example.com",
            phone_number="+571231231234",
            gender="MALE",
            country_id=self.country,
            picture="url_image"
        )

        self.category = category.objects.create(
            description="all_categories_test"
        )

        self.clothes = Clothes.objects.create(
            title="Test_title",
            description="Test_description",
            category_id=self.category,
            size="M",
            gender="MALE",
            user_id=self.username,
            brand="Test_brand",
            picture_1="url_image1",
            picture_2="url_image2"
        )

class SwapinManagerTestCase(SwapinTestCasesSetUp):
    """ Swapin manager testcase """

    def test_CreateToken(self):
        """Create Token for user """
        token = Token.objects.create(
            user=self.username
        )
        self.assertIsNotNone(token.key)
    
    def test_CreateClothes(self):
        """Create clothes when user send it"""
        clothes = Clothes.objects.create(
            title="Test_title",
            description="Test_description",
            category_id=self.category,
            size="M",
            gender="MALE",
            user_id=self.username,
            brand="Test_brand",
            picture_1="url_image1",
            picture_2="url_image2"
        )
        self.assertIsNotNone(clothes)

    def test_CreateLike(self):
        """Create like test """
        like_test = like.objects.create(
            type_like="SUPERLKE",
            user_id=self.username,
            clothe_id=self.clothes
        )
        self.assertIsNotNone(like_test)
    
    def test_CreateMatch(self):
        """ Create Match """
        match_test = Match.objects.create(
            user_like=self.username,
            user_clothe=self.username
        )
        self.assertIsNotNone(match_test)

class getNotificationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.access_token = '9789f67d74c0882c538a406f8befd032d810e84f'
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
