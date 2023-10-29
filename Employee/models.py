from django.db import models


# Create your models here.
class Department(models.Model):
    deptNo = models.CharField(max_length=5)
    deptName = models.CharField(max_length=50)

    def __str__(self):
        return self.deptNo + " " + self.deptName


class Employee(models.Model):
    deptNo = models.ForeignKey(Department, on_delete=models.CASCADE)
    empNo = models.CharField(max_length=5)
    empName = models.CharField(max_length=50)
    empAdd = models.CharField(max_length=100)

    def __str__(self):
        return self.empNo + " " + \
               "      " + self.empName + "   " + self.empAdd
