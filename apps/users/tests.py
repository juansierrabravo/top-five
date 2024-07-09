from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import is_password_usable

from apps.users.models import CustomUser, CustomUserManager


class UserModelTest(TestCase):

    def test_user_model_inherit_abstractbaseuser(self):
        self.assertTrue(issubclass(CustomUser, AbstractBaseUser))

    def test_user_model_manager_inherit_baseusermanager(self):
        self.assertTrue(issubclass(CustomUserManager, BaseUserManager))

    def test_create_new_user(self):
        user = CustomUser.objects.create_user(
            username="myusername",
            password="secure-password",
        )
        self.assertEqual(CustomUser.objects.count(), 1)

        saved_user = CustomUser.objects.first()

        self.assertEqual(saved_user, user)
        self.assertEqual(saved_user.username, "myusername")
        self.assertTrue(saved_user.check_password("secure-password"))
        self.assertTrue(saved_user.is_active)
        self.assertFalse(saved_user.is_staff)

    def test_create_new_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            username="mysuperusername",
            password="secure-superpassword",
        )
        self.assertEqual(CustomUser.objects.count(), 1)

        saved_superuser = CustomUser.objects.first()

        self.assertEqual(saved_superuser, superuser)
        self.assertEqual(saved_superuser.username, "mysuperusername")
        self.assertTrue(saved_superuser.check_password("secure-superpassword"))
        self.assertTrue(saved_superuser.is_active)
        self.assertTrue(saved_superuser.is_staff)

    def test_create_new_user_repeated_username(self):
        first_user = CustomUser.objects.create_user(
            username="firstuser",
            password="secure-password",
        )

        with self.assertRaises(IntegrityError):
            second_user = CustomUser.objects.create_user(
                username="firstuser",
                password="secure-password",
            )

    def test_create_new_user_missing_parameters(self):
        with self.assertRaises(TypeError):
            missing_username_user = CustomUser.objects.create_user(
                password="secure-password",
            )

        with self.assertRaises(TypeError):
            missing_password_user = CustomUser.objects.create_user(
                username="missingpasswordusername",
            )

    def test_create_new_user_empty_parameters(self):
        with self.assertRaises(ValueError):
            empty_username_user = CustomUser.objects.create_user(
                username="",
                password="secure-password",
            )

        with self.assertRaises(ValueError):
            empty_password_user = CustomUser.objects.create_user(
                username="emptypasswordusername",
                password="",
            )

    def test_create_new_user_with_none_values(self):
        with self.assertRaises(ValueError):
            none_username_user = CustomUser.objects.create_user(
                username=None,
                password="secure-password",
            )

        with self.assertRaises(ValueError):
            none_password_user = CustomUser.objects.create_user(
                username="emptypasswordusername",
                password=None,
            )

    def test_auth_user_model_equals_custom_user_model(self):
        pass

    def test_username_parses_to_lowercase(self):
        pass

    def test_username_max_length(self):
        pass

    def test_password_max_length(self):
        pass

    def test_model_configurations(self):
        pass