from django.db import models

# Create your models here.

class Comment(models.Model):
    opinion = [('Very Helpful','Very Helpful'),('Educative','Educative'),('Not Helpful','Not Helpful')]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField(null=True,help_text = u"Which features did you like, any improvement to be done...")
    opinion = models.CharField(max_length=100,choices=opinion)

    def __str__(self):
        return self.name