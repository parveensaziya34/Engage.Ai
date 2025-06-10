import os
from django.core.management.base import BaseCommand
import csv
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Send bulk emails to users listed in emails.csv'

    def handle(self, *args, **kwargs):
        # Get the directory of this file
        app_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to emails.csv
        csv_path = os.path.normpath(os.path.join(app_dir, '..', '..', 'emails.csv'))

        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR(f"File not found: {csv_path}"))
            return

        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recipient_email = row['email']
                recipient_name = row.get('name', '')
                subject = f"Hello {recipient_name}"
                message = "This is a test bulk email from Engage.AI"
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient_email],
                    fail_silently=False,
                )

        self.stdout.write(self.style.SUCCESS('Emails sent successfully!'))
