from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **other_fields):
        """Creates and saves an user with the given
        username and password."""
        if not username:
            raise ValueError(_("The field 'username' must be specified."))

        if not password:
            raise ValueError(_("The field 'password' must be specified."))

        user = self.model(username=username, **other_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **other_fields):
        """Creates and saves a superuser with the given
        username and password."""
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    alphanumeric_validator = RegexValidator(
        r"^[0-9a-zA-Z]*$", "Only alphanumeric characters are allowed."
    )

    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        help_text=_(
            "Required. 50 characters or fewer. Lowercase letters and digits only."
        ),
        validators=[alphanumeric_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    def save(self, *args, **kwargs):
        # Parse the username to lowercase before saving the record
        self.username = self.username.lower()
        super().save(*args, **kwargs)
