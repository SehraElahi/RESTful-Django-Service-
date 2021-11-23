#
from django.db import models
import datetime

# Create your models here.

class Professor (models.Model):
first_name = models.CharField(max_length=100)
last_name = models.CharField(max_length=100)
prof_id = models.CharField(max_length=3)

    def __str__ (self):
        return self.first_name + " " + self.last_name

class Module (models.Model):
name = models.CharField (max_length=100)
mod_code = models.CharField(max_length=3)
year_choice = [(r,r) for r in range(1984, datetime.date.today().year+1)]
year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
semester_choice (("1", "1"), ("2", "2"))
semester = models.CharField(max_length=1, default = '1', choices=semester_choice)
professor = models.ManytoManyField(Professor)

    def __str__ (self):
        return self.name


class Rating (model.Models):
rating_choice = ((1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'))
rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=rating_choice)
professor = models.ForeignKey(Professor)
module = models.ForeignKey( Module)
