from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

USER_GROUPS=(
    ('USER', "USER"),
    ('EDITOR', "EDITOR"),
    ('ADMIN', "ADMIN"),
)


class MyUserManager(BaseUserManager):
    def __create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_active', False)
        kwargs.setdefault('is_admin', False)
        user = self.__create_user(email, password, **kwargs)
        return user

    def create_superuser(self, email, password, **kwargs):
        if kwargs.get('group') != 'ADMIN':
            raise ValueError('Superuser must be in group ADMIN.')
        kwargs.setdefault('group', 'ADMIN')
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_active', True)

        user = self.__create_user(email, password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    group = models.CharField(max_length=50, choices=USER_GROUPS, default=USER_GROUPS[0][0])
    first_name = models.CharField(max_length=50, verbose_name="first name", blank=True)
    last_name = models.CharField(max_length=50, verbose_name="last name", blank=True)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['group', ]

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        if self.group == 'ADMIN':
            return True
        return False

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def premoderated_content(self):
        if self.group == 'USER':
            return True
        return False

    @property
    def is_staff(self):
        return self.is_admin
