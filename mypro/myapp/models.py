from django.db import models

# Create your models here.
class Department(models.Model):
    DeptNo = models.AutoField(primary_key=True)
    Dname = models.CharField(max_length=100, unique=True)
    Location = models.CharField(max_length=50)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.Dname


class Employee(models.Model):
    EmpId = models.AutoField(primary_key=True)
    Ename = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Gender = models.CharField(max_length=6)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100, unique=True)
    DOB = models.DateField(null=True, blank=True)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Address = models.CharField(max_length=150)

    DeptNo = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        db_column='DeptNo'
    )

    class Meta:
        db_table = 'Employee'

    def __str__(self):
        return self.Ename
