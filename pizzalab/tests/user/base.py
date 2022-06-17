from datetime import datetime

from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from user.models import User, Group, Profile, Address


class BaseUserTest(APITestCase):
    TEST_EMAIL = 'test@test.com'
    TEST_PASS = 'test'
    TEST_VALID_PASS = 'Test1!'

    def setUp(self):
        self.model = User
        self.user_group = Group.objects.create(name='Users')
        self.user = User.objects.create_user(email=self.TEST_EMAIL, password=self.TEST_PASS)


class BaseProfileTest(BaseUserTest):
    TEST_FIRST_NAME = 'Test'
    TEST_LAST_NAME = 'Case'
    TEST_PHONE = '123456789'
    TEST_BIRTH_DATE = datetime.now()

    def setUp(self):
        super().setUp()
        self.profile = Profile.objects.create(
            user=self.user,
            first_name=self.TEST_FIRST_NAME,
            last_name=self.TEST_LAST_NAME,
            phone=self.TEST_PHONE,
            birth_date=self.TEST_BIRTH_DATE
        )


class BaseAddressTest(BaseUserTest):
    TEST_CITY = 'Test city'
    TEST_STREET = 'Test street'
    TEST_HOUSE = 1

    def setUp(self):
        super().setUp()
        self.address = Address.objects.create(
            user=self.user,
            city=self.TEST_CITY,
            street=self.TEST_STREET,
            house=self.TEST_HOUSE
        )


class BaseUserAPITestCase(BaseProfileTest, BaseAddressTest):

    def setUp(self):
        super().setUp()
        self.users_url = reverse_lazy('users')
        self.user_url = reverse_lazy('user', kwargs={'pk': self.user.id})
        self.token_url = reverse_lazy('token')
        self.refresh_url = reverse_lazy('refresh')
