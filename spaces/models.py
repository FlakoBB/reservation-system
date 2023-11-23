from django.db import models
from users.models import MyUser

class SpaceType(models.Model):
  space_id = models.CharField(primary_key=True, unique=True, blank=False, max_length=30)
  space_name = models.CharField(max_length=60, blank=False)

  def __str__(self):
    return self.space_name

class CoworkingSpace(models.Model):
  name = models.CharField(max_length=100, blank=False)
  location = models.CharField(max_length=255, blank=False)
  city = models.CharField(max_length=100, blank=False)
  capacity = models.IntegerField(blank=False)
  is_available = models.BooleanField(default=True)
  space_type = models.ForeignKey(SpaceType, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} - {self.space_type.space_name}'

class Reservation(models.Model):
  user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
  space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE)
  reservation_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.space.name}: {self.user.username}'
