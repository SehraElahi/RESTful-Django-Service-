from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models import Max, Min

import datetime

# Create your models here.

class Professor (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    prof_id = models.CharField(max_length=3, default= "", verbose_name='ID', unique=True)

    def __str__ (self):
        return self.prof_id + ", " + self.first_name + " " + self.last_name
        # return self.name


class Module (models.Model):
    mod_code = models.CharField(max_length=3, default="", verbose_name='Module Code')
    name = models.CharField(max_length=100, default="", verbose_name='Module Name')
    year_choice = [(r,r) for r in range(1984, datetime.date.today().year+1)]
    year = models.IntegerField(choices=year_choice, default=datetime.datetime.now().year)
    semester_choice = (("1", "1"), ("2", "2"))
    semester = models.CharField(max_length=1, choices=semester_choice)
    professor = models.ManyToManyField(Professor)
    #
    def __str__ (self):
        return self.name + " " + self.mod_code

class Rating (models.Model):
    module = models.ForeignKey(Module, models.CASCADE)
    professor = models.ForeignKey(Professor, models.CASCADE)
    rating_choice = ((1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=1, choices=rating_choice)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return " Professor " + str(self.professor) + " for the module "  + str(self.module)
