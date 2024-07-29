from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length = 200, unique=True)


# class Phone(models.Model):
#
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='images/phones')
#     release_date = models.DateField()
#     lte_exists = models.BooleanField(default=False)
#     slug = models.SlugField(unique=True)
#     id = models.AutoField(primary_key=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name




