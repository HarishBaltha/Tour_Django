from django.db import models


class TourPlace(models.Model):
    no = models.AutoField(primary_key=True)
    Place = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    Inside_Places = models.CharField(max_length=300)
    Persons = models.CharField(max_length=100)
    Image = models.FileField(upload_to="files")
    Details = models.TextField()
    Marked_Price = models.PositiveIntegerField()
    Confirm_Price = models.PositiveIntegerField()
    Offer_Valid = models.DateTimeField()

    def __str__(self):
        return self.Place

class AdminModel(models.Model):
    Username = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100, unique=True)
