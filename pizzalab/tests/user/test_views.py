from rest_framework import status

from pizzalab.tests.user.base import BaseUserAPITestCase


class TestUser(BaseUserAPITestCase):
    TEST_ANOTHER_EMAIL = 'test.mail@gmail.com'

    def test__user_email_unique_constraint(self):
        signup_data = {
            'email': self.TEST_EMAIL,
            'password': self.TEST_VALID_PASS,
            'password_confirm': self.TEST_VALID_PASS
        }
        resp = self.client.post(self.users_url, signup_data, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', resp.data)
        self.assertEqual(len(resp.data['email']), 1)
        self.assertTrue(hasattr(resp.data['email'][0], 'code'))
        self.assertEqual(resp.data['email'][0].code, 'unique')

    def test__user_password_validation_without_uppercase(self):
        signup_data = {
            'email': self.TEST_ANOTHER_EMAIL,
            'password': self.TEST_VALID_PASS.lower(),
            'password_confirm': self.TEST_VALID_PASS.lower()
        }
        resp = self.client.post(self.users_url, signup_data, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', resp.data)
        self.assertEqual(len(resp.data['password']), 1)
        self.assertTrue(hasattr(resp.data['password'][0], 'code'))
        self.assertEqual(resp.data['password'][0].code, 'invalid')

    def test__user_password_validation_without_lowercase(self):
        signup_data = {
            'email': self.TEST_ANOTHER_EMAIL,
            'password': self.TEST_VALID_PASS.upper(),
            'password_confirm': self.TEST_VALID_PASS.upper()
        }
        resp = self.client.post(self.users_url, signup_data, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', resp.data)
        self.assertEqual(len(resp.data['password']), 1)
        self.assertTrue(hasattr(resp.data['password'][0], 'code'))
        self.assertEqual(resp.data['password'][0].code, 'invalid')

    def test__user_password_validation_without_digit(self):
        signup_data = {
            'email': self.TEST_ANOTHER_EMAIL,
            'password': ''.join(i for i in self.TEST_VALID_PASS if not i.isdigit()),
            'password_confirm': ''.join(i for i in self.TEST_VALID_PASS if not i.isdigit())
        }
        resp = self.client.post(self.users_url, signup_data, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', resp.data)
        self.assertEqual(len(resp.data['password']), 1)
        self.assertTrue(hasattr(resp.data['password'][0], 'code'))
        self.assertEqual(resp.data['password'][0].code, 'invalid')

    def test__user_password_validation_without_special(self):
        signup_data = {
            'email': self.TEST_ANOTHER_EMAIL,
            'password': ''.join(i for i in self.TEST_VALID_PASS if not i.isdigit() and i.isascii()),
            'password_confirm': ''.join(i for i in self.TEST_VALID_PASS if not i.isdigit() and i.isascii())
        }
        resp = self.client.post(self.users_url, signup_data, format='json')

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', resp.data)
        self.assertEqual(len(resp.data['password']), 1)
        self.assertTrue(hasattr(resp.data['password'][0], 'code'))
        self.assertEqual(resp.data['password'][0].code, 'invalid')

    def test__user_create_success(self):
        signup_data = {
            'email': self.TEST_ANOTHER_EMAIL,
            'password': self.TEST_VALID_PASS,
            'password_confirm': self.TEST_VALID_PASS
        }
        resp = self.client.post(self.users_url, signup_data, format='json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertIn('email', resp.data)
        self.assertEqual(resp.data['email'], self.TEST_ANOTHER_EMAIL)

        users_from_db = self.model.objects.filter(email=self.TEST_ANOTHER_EMAIL)
        self.assertTrue(users_from_db.exists())
        self.assertTrue(users_from_db.first().check_password(self.TEST_VALID_PASS))

    def test__user_retrieve_not_authenticated(self):
        resp = self.client.get(self.user_url)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', resp.data)
        self.assertTrue(hasattr(resp.data['detail'],  'code'))
        self.assertEqual(resp.data['detail'].code, 'not_authenticated')

    def test__user_retrieve_wrong_user(self):
        signup_data = {
            'email': self.TEST_ANOTHER_EMAIL,
            'password': self.TEST_VALID_PASS,
            'password_confirm': self.TEST_VALID_PASS
        }
        resp = self.client.post(self.users_url, signup_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        resp = self.client.post(self.token_url, {'email': self.TEST_ANOTHER_EMAIL, 'password': self.TEST_VALID_PASS})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {resp.data['access']}")
        resp = self.client.get(self.user_url)

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('detail', resp.data)
        self.assertTrue(hasattr(resp.data['detail'], 'code'))
        self.assertEqual(resp.data['detail'].code, 'permission_denied')

    def test__user_retrieve_valid_user(self):
        resp = self.client.post(self.token_url, {'email': self.TEST_EMAIL, 'password': self.TEST_PASS})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {resp.data['access']}")
        resp = self.client.get(self.user_url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], self.user.id)
