from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from Movies.soft_delete_app.models import SoftDeleteModel
from Movies.user_auth.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, SoftDeleteModel):
    """
    Extended User Model
    """
    HELP_TEXT_USERNAME = "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
    HELP_TEXT_IS_STAFF = "Designates whether the user can log into this admin site."
    ERROR_MSG_UNIQUE_USERNAME = "A user with that username already exists."

    USERNAME_MAX_LENGTH = 30

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        help_text=_(
            HELP_TEXT_USERNAME
        ),
        validators=[username_validator],
        error_messages={
            "unique": _(ERROR_MSG_UNIQUE_USERNAME),
        },
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(HELP_TEXT_IS_STAFF),
    )

    def __str__(self):
        return f'{self.username}'

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()
