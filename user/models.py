from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            password=None,
            first_name=None,
            last_name=None,
            is_staff=False,
            is_active=True,
            telephone=None,
            **extra_fields
        ):
        'Creates a User with a given first_name, last_name, email and password'
        email = UserManager.normalize_email(email)
        user = self.model(
            email=email, is_active=is_active,
            first_name=first_name, last_name=last_name,
            telephone=telephone,
            is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None, **extra_fields):
        return self.create_user(email, password, first_name, last_name, is_staff=True, is_superuser=True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', 
        unique=True)
    first_name =  models.CharField('first_name',
        max_length=256)
    last_name =  models.CharField('last_name',
        max_length=256, blank=True)
    is_staff = models.BooleanField('staff_status',
        default=False)
    is_active = models.BooleanField('active',
        default=True)
    date_joined = models.DateTimeField('date_joined',
        default=timezone.now, editable=True)
    telephone = models.CharField('phone_number',
        max_length=30, blank=True, unique=True)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telephone']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def get_very_first_name(self):
        return self.first_name.split(' ')[0]