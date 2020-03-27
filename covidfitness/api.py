from rest_framework import viewsets, permissions, mixins
from .serializers import ChallengeSerializer, UserChallengeSerializer, CompletedChallengeSerializer, UserProfileSerializer
from .models import Challenge, UserChallenge, CompletedChallenge, UserProfile

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = ChallengeSerializer

class AUTHUserChallengeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserChallengeSerializer

    def get_queryset(self):
        return self.request.user.challenges.all()

class UserChallengeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserChallenge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = UserChallengeSerializer

class AUTHCompletedChallengeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializer_class = CompletedChallengeSerializer

    def get_queryset(self):
        return self.request.user.completed.all()

class CompletedChallengeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CompletedChallenge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompletedChallengeSerializer

class AUTHUserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return self.request.user.completed.all()

class UserProfileViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserProfileSerializer