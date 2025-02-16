import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    print(f"Signal is running in thread: {threading.current_thread().name}")

print(f"Caller is running in thread: {threading.current_thread().name}")
user = User.objects.create(username="testuser")
