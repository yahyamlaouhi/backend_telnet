from email import header
from django.db import models
from pandas import DataFrame
import base64

class NUser(models.Model):
    NomPrenom=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Pwd1=models.CharField(max_length=50)
    Pwd2=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    Role=models.CharField(max_length=50)


class myuploadfile(models.Model):
    myfile = models.FileField(upload_to="")


class Table(models.Model):
    Date=models.CharField(max_length=50)
    Stamp=models.CharField(max_length=50)
    Direction=models.CharField(max_length=50)
    Source=models.CharField(max_length=50)
    Destination=models.CharField(max_length=50)
    MessageId=models.CharField(max_length=50)
    Length=models.CharField(max_length=50)
    StatusTx=models.CharField(max_length=50)
    Data=models.CharField(max_length=50)

class tablecsv(models.Model):
    header=models.CharField(max_length=50)
    data=models.CharField(max_length=500)

class tablecsvs(models.Model):
    datee=models.CharField(max_length=50)

class csvfile(models.Model):
    file = models.FileField(blank=False, null=False,upload_to='files/csv')
    description = models.CharField(null=True,max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class rapport(models.Model):
    annee=models.CharField(null=True,max_length=255)
    mois=models.CharField(null=True,max_length=255)
    jour=models.CharField(null=True,max_length=255)
    heure=models.CharField(null=True,max_length=255)
    minute=models.CharField(null=True,max_length=255)
    second=models.CharField(null=True,max_length=255)
    file=models.BinaryField (blank = True, null = True, editable = True)



class photosaver(models.Model):
    id_user=models.IntegerField(null=True,max_length=255)
    image=models.BinaryField (blank = True, null = True, editable = True)

