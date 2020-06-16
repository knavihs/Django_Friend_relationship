from django.db import models
from users.models import People
# Create your models here.

class Botschaft(models.Model):
    from_person = models.ForeignKey(People, related_name='from_person',on_delete= models.CASCADE)
    to_person = models.ForeignKey(People,related_name='to_person',on_delete= models.CASCADE)
    msg = models.TextField()
    