from django.db import models
from django.contrib.auth.models import User
from .widgets import DatePickerInput
from statements import widgets

# Create your models here.
class TeachersName(models.Model):
    name = models.CharField(max_length=200)
    
class HalaqaName(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class HalaqaType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class HalaqaCriteria(models.Model):
    criteria = models.CharField(max_length=200)

    def __str__(self):
        return self.criteria

class HalaqaTime(models.Model):
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.time
    
class Teachers(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    general_id = models.CharField(max_length=200, blank=True)
    financial_id = models.CharField(max_length=200, blank=True)
    halaqa_name = models.ForeignKey(HalaqaName, on_delete=models.PROTECT)
    halaqa_type = models.ForeignKey(HalaqaType, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'teachers'
    def __str__(self):
        return self.name

class Leave(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    halaqa_name = models.ForeignKey(HalaqaName, on_delete=models.PROTECT)
    halaqa_type = models.ForeignKey(HalaqaType, on_delete=models.DO_NOTHING)
    date_of_leave = models.DateField()
    date_of_return = models.DateField()

    def __str__(self):
        return str(self.owner)