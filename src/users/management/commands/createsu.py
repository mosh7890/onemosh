from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not get_user_model().objects.filter(username='admin').exists():
            get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'adminadmin', )
