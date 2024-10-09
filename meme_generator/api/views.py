from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MemeTemplate, Meme, Rating
from .serializers import MemeTemplateSerializer, MemeSerializer, RatingSerializer
from django.contrib.auth.models import User

class MemeTemplateListView(generics.ListAPIView):
    queryset = MemeTemplate.objects.all()
    serializer_class = MemeTemplateSerializer

class MemeListView(generics.ListAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

class MemeCreateView(generics.CreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MemeRetrieveView(generics.RetrieveAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

class MemeRateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



