from rest_framework import viewsets, permissions, mixins
from .serializers import ChallengeSerializer, UserChallengeSerializer, CompletedChallengeSerializer
from .models import Challenge, UserChallenge, CompletedChallenge

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