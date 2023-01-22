from django.db import models


class Vacancy(models.Model):
    position = models.CharField(db_column='Должность', max_length=40)
    salary = models.DecimalField(db_column='Заработная плата', max_digits=8, decimal_places=2)
    work_schedule = models.CharField(db_column='График работы', max_length=40)
    responsibilities = models.TextField('Описание')
    requirements = models.TextField('Описание')
    working_conditions = models.TextField('Описание')

    def __str__(self):
        return f'{self.position} {self.salary} {self.work_schedule} {self.responsibilities} {self.requirements} {self.working_conditions}'

