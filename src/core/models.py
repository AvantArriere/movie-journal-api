from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
     PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
