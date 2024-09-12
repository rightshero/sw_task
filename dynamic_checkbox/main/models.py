from django.db import models

possible_choices=(("A","A"), ("B","B"))

class checkbox(models.Model):
    level = models.AutoField(primary_key=True)
    choice = models.CharField(max_length=1, choices=possible_choices, default=None, blank=True, null=True) 

    def __str__(self):
        return self.choice