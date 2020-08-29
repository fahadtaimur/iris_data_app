from django.db import models

# Create your models here.
class Species(models.Model):
    species = models.CharField(max_length=200)

    def __str__(self):
        return self.species

class IrisData(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='specie')
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()

    def __str__(self):
        return f"{self.id} | {self.species}"
