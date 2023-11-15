from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
  is_admin = models.BooleanField(default=False)

  groups = models.ManyToManyField(
    "auth.Group",
    related_name="myuser_set",
    related_query_name="myuser",
    blank=True,
    help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
  )

  user_permissions = models.ManyToManyField(
    "auth.Permission",
    related_name="myuser_set",
    related_query_name="myuser",
    blank=True,
    help_text="Specific permissions for this user.",
  )
