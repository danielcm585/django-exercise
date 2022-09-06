from django.db import models

class WishlistItem(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.TextField()
  