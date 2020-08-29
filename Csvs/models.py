from django.db import models

# Create your models here.
class Csv(models.Model):
    filename = models.FileField(upload_to="csv/")

    def __str__(self):
        return "File Id: {}".format(self.id)