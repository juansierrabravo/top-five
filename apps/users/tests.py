from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.utils import DataError
from django.test import TestCase

from apps.users.models import CustomUser
from apps.users.forms import CustomAuthenticationForm


class CustomUserUserModelTest(TestCase):

    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            username="myusername",
            password="secure-password",
        )

    def test_custom_user_model_is_set_as_project_user_model(self):
        """Confirm that the CustomUser model is set as the project's
        user model."""
        self.assertEqual(CustomUser, get_user_model())

    def test_custom_user_model_username_field(self):
        """Confirm that the USERNAME_FIELD in the CustomUser model is set to
        'username'."""
        self.assertEqual(CustomUser.USERNAME_FIELD, "username")

    def test_create_user_with_valid_credentials(self):
        """Test the creation of a standard user with valid username
        and password to ensure proper storage and attribute settings."""
        self.assertEqual(CustomUser.objects.count(), 1)

        saved_user = CustomUser.objects.first()

        self.assertEqual(saved_user, self.test_user)
        self.assertEqual(saved_user.username, "myusername")
        self.assertTrue(saved_user.check_password("secure-password"))
        self.assertTrue(saved_user.is_active)
        self.assertFalse(saved_user.is_staff)
        self.assertFalse(saved_user.is_superuser)

    def test_create_superuser_with_valid_credentials(self):
        """Test the creation of a standard superuser with valid username
        and password to ensure proper storage and attribute settings."""
        superuser = CustomUser.objects.create_superuser(
            username="mysuperusername",
            password="secure-superpassword",
        )
        self.assertEqual(CustomUser.objects.count(), 2)

        saved_superuser = CustomUser.objects.last()

        self.assertEqual(saved_superuser, superuser)
        self.assertEqual(saved_superuser.username, "mysuperusername")
        self.assertTrue(saved_superuser.check_password("secure-superpassword"))
        self.assertTrue(saved_superuser.is_active)
        self.assertTrue(saved_superuser.is_staff)
        self.assertTrue(saved_superuser.is_superuser)

    def test_username_must_be_unique(self):
        """Ensure that the username field is unique across users by expecting
        an IntegrityError when attempting to create a user with a duplicate
        username."""
        with self.assertRaises(IntegrityError):
            user = CustomUser.objects.create_user(
                username="myusername",
                password="secure-password",
            )

    def test_create_user_without_username_raises_error(self):
        """Test that creating a user without specifying a username results
        in appropriate exceptions being raised for missing, empty, or null
        usernames."""
        NO_USERNAME_ERROR_MESSAGE = "The field 'username' must be specified."

        with self.assertRaises(TypeError) as error:
            missing_username_user = CustomUser.objects.create_user(
                password="secure-password",
            )
        self.assertIn("missing 1 required positional argument", str(error.exception))

        with self.assertRaisesMessage(ValueError, NO_USERNAME_ERROR_MESSAGE):
            empty_username_user = CustomUser.objects.create_user(
                username="",
                password="secure-password",
            )

        with self.assertRaisesMessage(ValueError, NO_USERNAME_ERROR_MESSAGE):
            none_username_user = CustomUser.objects.create_user(
                username=None,
                password="secure-password",
            )

    def test_create_user_without_password_raises_error(self):
        """Test that creating a user without specifying a password results
        in appropriate exceptions being raised for missing, empty, or null
        passwords."""
        NO_PASSWORD_ERROR_MESSAGE = "The field 'password' must be specified."

        with self.assertRaises(TypeError) as error:
            missing_password_user = CustomUser.objects.create_user(
                username="johndoe",
            )
        self.assertIn("missing 1 required positional argument", str(error.exception))

        with self.assertRaisesMessage(ValueError, NO_PASSWORD_ERROR_MESSAGE):
            empty_password_user = CustomUser.objects.create_user(
                username="johndoe",
                password="",
            )

        with self.assertRaisesMessage(ValueError, NO_PASSWORD_ERROR_MESSAGE):
            none_password_user = CustomUser.objects.create_user(
                username="johndoe",
                password=None,
            )

    def test_username_is_saved_as_lowercase(self):
        """Ensure that all usernames are saved in lowercase regardless
        of the case of the input provided."""
        user = CustomUser.objects.create_user(
            username="JohnDoe",
            password="secure-password",
        )
        self.assertEqual(user.username, "johndoe")

    def test_username_exceeding_max_length_raises_error(self):
        """Check that trying to create a username longer than the maximum allowed
        length results in a DataError."""
        USERNAME_MAX_LENGTH = CustomUser._meta.get_field("username").max_length
        username_at_max = "u" * USERNAME_MAX_LENGTH
        username_beyond_max = "u" * (USERNAME_MAX_LENGTH + 1)

        # Create an user with the username length limit
        first_user = CustomUser.objects.create_user(
            username=username_at_max,
            password="secure-password",
        )

        # Create an user with the username length limit plus 1 character
        with self.assertRaises(DataError):
            second_user = CustomUser.objects.create_user(
                username=username_beyond_max,
                password="secure-password",
            )

    def test_username_rejects_spaces(self):
        """Ensure that ValidationError is raised if the username contains
        spaces."""

        NON_ALPHANUMERIC_CHARACTERS_ERROR_MESSAGE = (
            "Only alphanumeric characters are allowed."
        )

        with self.assertRaisesMessage(
            ValidationError, NON_ALPHANUMERIC_CHARACTERS_ERROR_MESSAGE
        ):
            CustomUser.objects.create_user(
                username="my username", password="secure-password"
            ).full_clean()

    def test_username_rejects_special_characters(self):
        """Ensure that ValidationError is raised if the username contains
        special characters like '@', '-', etc."""

        NON_ALPHANUMERIC_CHARACTERS_ERROR_MESSAGE = (
            "Only alphanumeric characters are allowed."
        )

        # Make the same test with different special characters
        special_chars = ["@", "-", "#", "!", "*"]
        for char in special_chars:
            with self.assertRaisesMessage(
                ValidationError, NON_ALPHANUMERIC_CHARACTERS_ERROR_MESSAGE
            ):
                CustomUser.objects.create_user(
                    username=f"my{char}username", password="secure-password"
                ).full_clean()


class CustomAuthenticationFormTest(TestCase):

    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            username="myusername",
            password="secure-password",
        )

    def validate_missing_required_field_in_form(self, field_name, form):
        self.assertIn(field_name, form.errors)
        self.assertIn("This field is required.", form.errors[field_name])

    def test_authentication_form_valid(self):
        """Test form is valid when the user types valid credentials."""
        form_data = {
            "username": "myusername",
            "password": "secure-password",
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_authentication_form_fails_with_invalid_credentials(self):
        """Test form is not valid when the credentials are not valid."""
        form_data = {
            "username": "myusername",
            "password": "wrong-password",
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)
        self.assertIn(
            "Please enter a correct username and password. Note that both fields may be case-sensitive.",
            form.errors["__all__"],
        )

    def test_authentication_form_fails_with_empty_username(self):
        """Test form is not valid when the field 'username' is empty."""
        form_data = {
            "username": "",
            "password": "secure-password",
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.validate_missing_required_field_in_form("username", form)

    def test_authentication_form_fails_with_null_username(self):
        """Test form is not valid when the field 'username' is null."""
        form_data = {
            "username": None,
            "password": "secure-password",
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.validate_missing_required_field_in_form("username", form)

    def test_authentication_form_fails_with_empty_password(self):
        """Test form is not valid when the field 'password' is empty."""
        form_data = {
            "username": "myusername",
            "password": "",
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.validate_missing_required_field_in_form("password", form)

    def test_authentication_form_fails_with_null_password(self):
        """Test form is not valid when the field 'password' is null."""
        form_data = {
            "username": "myusername",
            "password": None,
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.validate_missing_required_field_in_form("password", form)
