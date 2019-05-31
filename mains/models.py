from django.db import models

class event(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateField()
#    heroes = models.CharField(max_length = 200)

def _str_(self):
    return self.title


class heroe(models.Model):
    name = models.CharField(max_length = 100)
    biography = models.TextField()
    rewards = models.TextField()
    lived = models.CharField(max_length = 100)
    participant = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

def _str_(self):
    return self.name
