from django.db import models

# Create your models here.

class Contact(models.Model):
    # hey django make files of table of this datas every data is saved in every collumn
    # its like an excel sheet table and every variable is like cols of every datas
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    description=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name