from django.db import models



class heroe(models.Model):
    name = models.CharField(max_length = 100)
    biography = models.TextField()
    rewards = models.TextField()
    lived = models.CharField(max_length = 100)
    army = models.ForeignKey('army', on_delete=models.CASCADE, null=True)
    took_part = models.ForeignKey('event', on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.name

class event(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    result = models.TextField()
    participants = models.ManyToManyField(heroe)
#    date = models.DateField()
#    heroes = models.CharField(max_length = 200)

    def _str_(self):
        return self.title

class army(models.Model):
    name = models.CharField(max_length = 100)
    took_part_events = models.ManyToManyField(event)
#    heroes = models.ForeignKey(heroe, on_delete=models.CASCADE, null=True)
    comander = models.CharField(max_length = 100)

    def _str_(self):
        return self.name


class date(models.Model):
    date = models.DateField()
    date_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

class place(models.Model):
    place = models.CharField(max_length = 200)
    place_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)
