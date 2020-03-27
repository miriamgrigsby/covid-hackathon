from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    workout_type=models.CharField(max_length=200)
    reps=models.IntegerField()
    sport=models.TextField()

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