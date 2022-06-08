from django.db import models


# Create your models here.
class Booktbl(models.Model):
    id = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    rule = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    img = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booktbl'

