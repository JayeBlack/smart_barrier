# apps/officer_auth/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid


class OfficerManager(BaseUserManager):
    def create_user(self, email, badge_number, name, username=None, password=None):
        if not email:
            raise ValueError("Officers must have an email address")
        if not badge_number:
            raise ValueError("Officers must have a badge number")
        user = self.model(
            email=self.normalize_email(email),
            badge_number=badge_number,
            name=name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, badge_number, name, username=None, password=None):
        user = self.create_user(email, badge_number, name, username, password)
        user.role = "admin"
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Officer(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    password_hash = models.CharField(max_length=128)
    role = models.CharField(max_length=50, default="officer")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = OfficerManager()

    USERNAME_FIELD = 'email'  # Kept for creation, overridden for login
    REQUIRED_FIELDS = ['badge_number', 'name']

    def __str__(self):
        return f"{self.name} ({self.badge_number})"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
