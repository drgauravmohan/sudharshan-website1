import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medantaclone.settings')
os.environ.setdefault('SECRET_KEY', 'sudharshan-heart-clinic-secret-2024-xyz')
os.environ.setdefault('ALLOWED_HOSTS', '*')
os.environ.setdefault('DEBUG', 'False')

django.setup()

from django.contrib.auth.models import User

# Delete any existing admin and recreate fresh
User.objects.filter(username='admin').delete()
User.objects.create_superuser(
    username='admin',
    email='admin@gmail.com',
    password='Admin@1234'
)
print("✅ Admin created: username=admin password=Admin@1234")
