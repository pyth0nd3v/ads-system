from django.db import models
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    keyword = models.CharField(max_length=3)
    max_daily_visitors = models.IntegerField()

    def __str__(self):
        return self.name + " - " + self.keyword


class Ad(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cities = models.ManyToManyField(Location, related_name='ads')
    start_date = models.DateField()
    end_date = models.DateField()
    visitors_per_day = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
