from datetime import datetime

from rest_framework import test

from user.models import User, Group, Profile


class BaseUserTest(test.APITestCase):
    TEST_EMAIL = 'test@test.com'
    TEST_PASS = 'test'

    def setUp(self):
        self.user_group = Group.objects.create(name='Users')
        self.user = User.objects.create_user(email=self.TEST_EMAIL)
        self.user.set_password(self.TEST_PASS)


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
