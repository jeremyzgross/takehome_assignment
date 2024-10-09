from django.db import models
from django.contrib.auth.models import User

# Model for MemeTemplate
class MemeTemplate(models.Model):
    name = models.CharField(max_length=100)  # Name of the meme template
    image_url = models.URLField()  # URL of the meme template image
    default_top_text = models.CharField(max_length=100, blank=True)  # Default top text for the meme
    default_bottom_text = models.CharField(max_length=100, blank=True)  # Default bottom text for the meme

# Model for Meme
class Meme(models.Model):
    template = models.ForeignKey(MemeTemplate, on_delete=models.CASCADE)  # Foreign key to MemeTemplate
    top_text = models.CharField(max_length=100)  # Top text of the meme
    bottom_text = models.CharField(max_length=100)  # Bottom text of the meme
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the meme
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the meme was created

# Model for Rating
class Rating(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name='ratings')  # Foreign key to Meme
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who rated the meme
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Score given by the user (1-5)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the rating was created

    class Meta:
        unique_together = ('meme', 'user')  # Ensures each user can only rate a meme once