import os
from django.core.management.base import BaseCommand
from ...models import DailyMile

def miles():
    DailyMile(day=1, distance="1 mile").save()
    DailyMile(day=2, distance="1 mile").save()
    DailyMile(day=3, distance="1 mile").save()
    DailyMile(day=4, distance="1 mile").save()
    DailyMile(day=5, distance="1 mile").save()
    DailyMile(day=6, distance="1 mile").save()
    DailyMile(day=7, distance="1 mile").save()
    DailyMile(day=8, distance="1 mile").save()
    DailyMile(day=9, distance="1 mile").save()
    DailyMile(day=10, distance="1 mile").save()
    DailyMile(day=11, distance="1 mile").save()
    DailyMile(day=12, distance="1 mile").save()
    DailyMile(day=13, distance="1 mile").save()
    DailyMile(day=14, distance="1 mile").save()
    DailyMile(day=15, distance="1 mile").save()
    DailyMile(day=16, distance="1 mile").save()
    DailyMile(day=17, distance="1 mile").save()
    DailyMile(day=18, distance="1 mile").save()
    DailyMile(day=19, distance="1 mile").save()

def clear_data():
    DailyMile.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        miles()
        print("completed")