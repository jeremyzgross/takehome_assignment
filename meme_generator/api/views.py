from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MemeTemplate, Meme, Rating
from .serializers import MemeTemplateSerializer, MemeSerializer, RatingSerializer
from django.contrib.auth.models import User
from django.db.models import Avg

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

    def post(self, request, id):
        # Get the meme object
        try:
            meme = Meme.objects.get(id=id)
        except Meme.DoesNotExist:
            return Response({"detail": "Meme not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get the score from the request data
        score = request.data.get('score')

        # Validate the score
        if score is None or score < 1 or score > 5:
            return Response({"detail": "Invalid score. Must be between 1 and 5."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the rating
        rating = Rating.objects.create(meme=meme, user=request.user, score=score)

        return Response({"detail": "Rating created successfully.", "rating": RatingSerializer(rating).data}, status=status.HTTP_201_CREATED)

class RandomMemeView(generics.ListAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

    def get_queryset(self):
        return Meme.objects.order_by('?').first()


class TopMemesView(generics.ListAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

    def get_queryset(self):
        return Meme.objects.annotate(average_rating=Avg('ratings__score')).order_by('-average_rating')[:10]
