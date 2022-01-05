from django.db import models
from twilio.rest import Client

# Create your models here.

class Comment(models.Model):
    opinion = [('Very Helpful','Very Helpful'),('Educative','Educative'),('Not Helpful','Not Helpful')]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField(null=True,help_text = u"Which features did you like, any improvement to be done...")
    opinion = models.CharField(max_length=100,choices=opinion)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return self.name

    # def __str__ (self):
    #     return str(self.name)

    # def save(self,*args,**kwargs):
    #     account_sid='AC41cc2b25fdfb3f6d6a8b7ef353398d7e'
    #     auth_token='1d42a07c1f331cc71547a5c38c3e750d'
    #     client=Client(account_sid,auth_token)

    #     message= client.messages.create(
    #                     body=f'Message from {self.name},email {self.email},with a suggestion that {self.comment} and feels like the web app is {self.opinion}.',
    #                     from_='+14422449654',
    #                     to='+254791061506'
    #             )
    #     print(message.sid)
    #     return super().save(*args,**kwargs)