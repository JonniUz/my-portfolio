from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    link = models.CharField(max_length=2558)
    image = models.CharField(max_length=2558, null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_num = models.CharField(max_length=16)
    message = models.TextField()

    def __str__(self):
        return self.full_name
