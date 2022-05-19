from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        if 'is_staff' in kwargs and kwargs.get('is_staff'):
            group = Group.objects.get(name='Admins')
        else:
            group = Group.objects.get(name='Users')
        user.groups.set((group,))

        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email, password, **kwargs)
