from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create_superuser(
            'admin', 'luke.perrottet@hogarthww.com', 'admin'
            )
        user.save()
