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
    #     account_sid='AC8877e9137b57e99ec7b7641d59db0823'
    #     auth_token='92c2b8d41a8f2ae102838bc0711edbd3'
    #     client=Client(account_sid,auth_token)

    #     message= client.messages.create(
    #                     body=f'Message from {self.name},email {self.email},with a suggestion that {self.comment} and feels like the web app is {self.opinion}.',
    #                     from_='+18454788560',
    #                     to='+254754389371'
    #             )
    #     print(message.sid)
    #     return super().save(*args,**kwargs)