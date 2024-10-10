from django.contrib import admin
from .models import MemeTemplate, Meme, Rating  # Import models to register

# Register your models here.
admin.site.register(MemeTemplate)  # Register MemeTemplate model
admin.site.register(Meme)  # Register Meme model
admin.site.register(Rating)  # Register Rating model