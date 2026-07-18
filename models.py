from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    eloc = models.CharField(max_length=50)
    esal = models.IntegerField()

    # Returns name property as readable text layout inside admin overview panels
    def __str__(self):
        return self.ename