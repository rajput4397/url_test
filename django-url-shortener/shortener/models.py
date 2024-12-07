# shortener/models.py
from django.db import models
from django.utils import timezone
import uuid

class URL(models.Model):
    # 1. Original URL (Primary Key)
    url = models.URLField(unique=True)  # The original long URL
    
    # 2. Tiny URL (Unique)
    tiny_url = models.CharField(max_length=20, unique=True)  # Shortened URL
    
    # 3. Access count (Default is 0)
    access_count = models.PositiveIntegerField(default=0)  # Access counter
    
    # 4. Generation time (Timestamp)
    generation_time = models.DateTimeField(default=timezone.now)  # When the URL was shortened
    
    # 5. Expiration time (Default is 1 day from now)
    expiration_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))  # Expiration time
    
    def __str__(self):
        return self.url

    # Method to generate a short URL using UUID
    def generate_tiny_url(self):
        return str(uuid.uuid4().hex[:6])  # Returns first 6 characters of UUID as tiny URL
