from rest_framework import serializers
from .models import MemeTemplate, Meme, Rating

class MemeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemeTemplate
        fields = ['id', 'name', 'image_url', 'default_top_text', 'default_bottom_text']

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ['id', 'template', 'top_text', 'bottom_text', 'created_by', 'created_at']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'meme', 'user', 'score', 'created_at']
        read_only_fields = ['user', 'created_at']  # User should be set automatically
