from .models import Challenge, UserChallenge, CompletedChallenge, UserProfile
from rest_framework import serializers

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = ('id', 'time_created', 'challenge', 'user', 'repeat', 'failed', 'completed_challenges')

class CompletedChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedChallenge
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'