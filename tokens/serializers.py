from .models import Tokens
from rest_framework import serializers

class TokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = '__all__'
