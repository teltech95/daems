# import random
# import string
# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# # Create your models here.


# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model where the email address is the unique identifier
#     and has an is_admin field to allow access to the admin app
#     """

#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError(_("The email must be set"))
#         if not password:
#             raise ValueError(_("The password must be set"))
#         email = self.normalize_email(email)

#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('role', 1)

#         if extra_fields.get('role') != 1:
#             raise ValueError('Superuser must have role of Global Admin')
#         return self.create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     ADMIN = 1
#     USER = 2

#     ROLE_CHOICES = (
#         (ADMIN, 'Admin'),
#         (USER, 'User')

#     )
#     username = models.CharField(_('Username'), max_length=20, unique=True)
#     email = models.CharField(_('Email'), max_length=80, unique=True)
#     role = models.IntegerField(
#         choices=ROLE_CHOICES, blank=True, null=True, default=2)
#     first_name = models.CharField(_('First_name'), max_length=200, unique=True)
#     last_name = models.CharField(_('Last_name'), max_length=200, unique=True)
#     date_joined = models.DateTimeField(_('Date'), auto_now_add=True)

#     REQUIRED_FIELDS = ['email']
#     USERNAME_FIELD = 'username'

#     objects = CustomUserManager()

#     def __str__(self):
#         return f"User {self.email}"
