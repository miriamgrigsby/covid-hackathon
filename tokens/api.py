from rest_framework import viewsets, permissions, mixins
from .serializers import TokensSerializer
from .models import Tokens

class TokensViewSet(viewsets.ModelViewSet):
    queryset = Tokens.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = TokensSerializer

