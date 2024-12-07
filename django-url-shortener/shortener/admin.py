from django.contrib import admin
from .models import URL  # Import your model

admin.site.register(URL)  # Register the model to make it visible in the admin
