from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.

class People(models.Model):
    Name = models.CharField(max_length=20)
    Username = models.CharField(max_length=10,unique=True)
    Password = models.CharField(max_length=10)
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to+')
    def __str__(self):
        return self.Name

    def add_relationship(self, people):
        relationship, created = Relationship.objects.get_or_create(
            from_person=self,
            to_person=people,
        )
        return relationship

    def get_friends(self):
        return self.relationships.filter(
            to_people__from_person=self,
            from_people__to_person=self)

    '''def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)'''


class Relationship(models.Model):
    from_person = models.ForeignKey(People, related_name='from_people',on_delete=models.CASCADE)
    to_person = models.ForeignKey(People, related_name='to_people',on_delete=models.CASCADE)


class Posts(models.Model):
    post_of = models.ForeignKey(People,on_delete=models.CASCADE,null=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)

    def givelikes(self):
        self.likes += 1
        return self.likes

