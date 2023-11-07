from django.db import models

class Role(models.Model):
  role_id = models.CharField(primary_key=True, unique=True, blank=False, max_length=30)
  role_name = models.CharField(max_length=60, blank=False)

  def __str__(self):
    return self.role_name

class User(models.Model):
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=60)
  role = models.ForeignKey(Role, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
