from django.test import TestCase
from django.db import IntegrityError
from django.db.utils import DataError
from django.contrib.auth import get_user_model

from apps.users.models import CustomUser


class UserModelTest(TestCase):

    def test_create_user(self):
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
        self.assertFalse(saved_user.is_superuser)

    def test_create_superuser(self):
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
        self.assertTrue(saved_superuser.is_superuser)

    def test_user_unique_username(self):
        first_user = CustomUser.objects.create_user(
            username="firstuser",
            password="secure-password",
        )

        with self.assertRaises(IntegrityError):
            second_user = CustomUser.objects.create_user(
                username="firstuser",
                password="secure-password",
            )

    def test_create_user_no_username(self):
        with self.assertRaises(TypeError):
            missing_username_user = CustomUser.objects.create_user(
                password="secure-password",
            )

        with self.assertRaises(ValueError):
            empty_username_user = CustomUser.objects.create_user(
                username="",
                password="secure-password",
            )

        with self.assertRaises(ValueError):
            none_username_user = CustomUser.objects.create_user(
                username=None,
                password="secure-password",
            )

    def test_create_user_no_password(self):
        with self.assertRaises(TypeError):
            missing_password_user = CustomUser.objects.create_user(
                username="myusername",
            )

        with self.assertRaises(ValueError):
            empty_password_user = CustomUser.objects.create_user(
                username="myusername",
                password="",
            )

        with self.assertRaises(ValueError):
            none_password_user = CustomUser.objects.create_user(
                username="myusername",
                password=None,
            )

    def test_username_saved_in_lowercase(self):
        user = CustomUser.objects.create_user(
            username="MyUsername",
            password="secure-password",
        )
        self.assertEqual(user.username, "myusername")

    def test_username_max_length(self):
        username = "u" * 50
        first_user = CustomUser.objects.create_user(
            username=username,
            password="secure-password",
        )

        with self.assertRaises(DataError):
            second_user = CustomUser.objects.create_user(
                username=username + "u",
                password="secure-password",
            )

    def test_username_field(self):
        self.assertEqual(CustomUser.USERNAME_FIELD, "username")

    def test_auth_user_model_equals_custom_user_model(self):
        self.assertEqual(CustomUser, get_user_model())