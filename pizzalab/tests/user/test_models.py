from pizzalab.tests.user.base import BaseUserTest, BaseProfileTest


class TestUser(BaseUserTest):

    def test__user_contains_necessary_fields(self):
        user_fields = [i.name for i in self.user._meta.fields]

        self.assertIn('email', user_fields)
        self.assertIn('password', user_fields)
        self.assertIn('is_staff', user_fields)
        self.assertIn('is_superuser', user_fields)
        self.assertIn('updated_at', user_fields)
        self.assertIn('created_at', user_fields)

    def test__user_default_group(self):
        self.assertTrue(self.user.groups.first(), self.user_group)


class TestProfile(BaseProfileTest):

    def test__user_contains_necessary_fields(self):
        profile_fields = [i.name for i in self.profile._meta.fields]

        self.assertIn('user', profile_fields)
        self.assertIn('first_name', profile_fields)
        self.assertIn('last_name', profile_fields)
        self.assertIn('phone', profile_fields)
        self.assertIn('birth_date', profile_fields)
        self.assertIn('updated_at', profile_fields)
        self.assertIn('created_at', profile_fields)
