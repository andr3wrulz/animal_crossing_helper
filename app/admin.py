from django.contrib import admin

# Import the data classes
from .models import Creature

# Enable editing on the admin page
admin.site.register(Creature)