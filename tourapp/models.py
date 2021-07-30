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

class RegisterModel(models.Model):
    Name = models.CharField(max_length=30)
    Username = models.CharField(max_length=30, unique=True)
    Email = models.EmailField(max_length=20, unique=True)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=120, null=True, blank=True)
    Joined_on = models.DateTimeField(auto_now_add=True)
    Password1 = models.CharField(max_length=15, unique=True)
    Password2 = models.CharField(max_length=15)
    Secret_Info = models.CharField(max_length=200)

    def __str__(self):
        return self.Username

class LoginModel(models.Model):
    Username = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100, unique=True)

