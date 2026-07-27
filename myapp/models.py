from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    eloc = models.CharField(max_length=50)
    esal = models.IntegerField()

    # Returns name property as readable text layout inside admin overview panels
    def __str__(self):
        return self.ename

class Product(models.Model):
    pid=models.AutoField
    pname=models.CharField(max_length=100)
    pcat=models.CharField(max_length=100)
    pprice=models.IntegerField(default=0)
    pdate=models.DateField()
    pimage=models.ImageField(upload_to="myapp/image")
    def __str__(self):
        return self.pname
