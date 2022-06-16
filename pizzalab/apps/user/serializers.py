from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import Address
from user.models import User
from user.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'phone'
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = (
            'id',
            'user',
        )


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'profile',
            'address'
        )
        read_only_fields = (
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
        )

    def update(self, instance, validated_data: dict):
        profile_data = validated_data.pop('profile', None)
        address_data = validated_data.pop('address', None)

        for key, value in validated_data.items():
            if hasattr(instance, key):
                setattr(instance, key, value)

        instance.save(update_fields=validated_data)

        if profile_data:
            Profile.objects.update_or_create(user=instance, defaults=profile_data)

        if address_data:
            Address.objects.update_or_create(user=instance, defaults=address_data)

        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password',
            'password_confirm'
        )

    def _has_no_spaces(self, password: str):
        return not ' ' in password

    def _has_one_uppercase_character(self, password: str):
        return any(i.isupper() for i in password)

    def _has_one_lowercase_character(self, password: str):
        return any(i.isupper() for i in password)

    def _has_one_digit(self, password: str):
        return any(i.isdigit() for i in password)

    def _hast_one_special_character(self, password: str):
        return any(i.isascii() and not i.isdigit() for i in password)

    def validate_password(self, password: str):
        if (
            self._has_no_spaces(password) and
            self._has_one_digit(password) and
            self._hast_one_special_character(password) and
            self._has_one_uppercase_character(password) and
            self._has_one_lowercase_character(password)
        ):
            return password
        raise ValidationError(
            'Password must have:\n'
            '1. No spaces\n'
            '2. At least 1 digit\n'
            '3. At least 1 uppercase character\n'
            '4. At least 1 lowercase character\n'
            '5. At least 1 special character'
        )

    def validate(self, attrs):
        if attrs.get('password') == attrs.get('password_confirm'):
            attrs.pop('password_confirm')
            return attrs
        raise ValidationError('Passwords don\'t match')

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data.get('email'))
        user.set_password(validated_data.get('password'))
        return user
