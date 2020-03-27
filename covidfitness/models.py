from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    title=models.CharField(max_length=200)
    workout_type=models.CharField(max_length=200)
    reps=models.IntegerField()
    sport=models.TextField()
    daily=models.BooleanField(blank=True)
    points=models.IntegerField()

class UserChallenge(models.Model):
    time_created=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, related_name="challenges", on_delete=models.CASCADE)
    challenge=models.ForeignKey(Challenge, related_name="users", on_delete=models.CASCADE)
    failed=models.BooleanField(blank=True)
    repeat=models.BooleanField(default=True)

class CompletedChallenge(models.Model):
    user_challenge=models.ForeignKey(UserChallenge, related_name="completed_challenges", on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='challenge_photos', blank=True)
    user=models.ForeignKey(User, related_name="completed", on_delete=models.CASCADE)
    date_created=models.DateField(auto_now_add=True)

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female',),
        ('M', 'Male'),
        ('O', 'Other')
    ]
    points=models.IntegerField(null=True, default=0)
    city=models.CharField(max_length=200, null=True, blank=True)
    country=models.CharField(max_length=200, null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    photo=models.ImageField(upload_to="challenge_photos", null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200, null=True, blank=True)
    gender=models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    email=models.EmailField()
    user=models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
