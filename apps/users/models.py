from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
        return self.create_user(username, password, **other_fields)


class CustomUser(AbstractBaseUser):

    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        help_text=_(
            "Required. 50 characters or fewer. Lowercase letters and digits only."
        ),
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
