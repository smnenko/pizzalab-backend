from pizzalab.tests.user.base import BaseUserTest, BaseProfileTest, BaseAddressTest


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

    def test__profile_contains_necessary_fields(self):
        profile_fields = [i.name for i in self.profile._meta.fields]

        self.assertIn('user', profile_fields)
        self.assertIn('first_name', profile_fields)
        self.assertIn('last_name', profile_fields)
        self.assertIn('phone', profile_fields)
        self.assertIn('birth_date', profile_fields)
        self.assertIn('updated_at', profile_fields)
        self.assertIn('created_at', profile_fields)

    def test__profile_valid_max_length(self):
        first_name_max_length = self.profile._meta.get_field('first_name').max_length
        last_name_max_length = self.profile._meta.get_field('last_name').max_length
        phone_max_length = self.profile._meta.get_field('phone').max_length

        self.assertEqual(first_name_max_length, 256)
        self.assertEqual(last_name_max_length, 256)
        self.assertEqual(phone_max_length, 13)


class TestAddress(BaseAddressTest):

    def test__address_contains_necessary_fields(self):
        address_fields = [i.name for i in self.address._meta.fields]

        self.assertIn('city', address_fields)
        self.assertIn('street', address_fields)
        self.assertIn('house', address_fields)
        self.assertIn('building', address_fields)
        self.assertIn('floor', address_fields)
        self.assertIn('apartment', address_fields)
        self.assertIn('updated_at', address_fields)
        self.assertIn('created_at', address_fields)

    def test__profile_valid_max_length(self):
        city_max_length = self.address._meta.get_field('city').max_length
        street_max_length = self.address._meta.get_field('street').max_length

        self.assertEqual(city_max_length, 256)
        self.assertEqual(street_max_length, 256)
