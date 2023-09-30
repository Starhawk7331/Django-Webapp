from django.db import models

class Family_members(models.Model):
    firstname = models.CharField(max_length=255)
    secondname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    username = models.CharField(null=True)
    password = models.CharField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.secondname} {self.lastname}"
