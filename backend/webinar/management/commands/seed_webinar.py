from django.core.management.base import BaseCommand
from webinar.models import Setting, Speaker, AgendaItem

class Command(BaseCommand):
    help = 'Seeds the database with default webinar data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # 1. Settings
        settings_data = {
            'site_title': 'Svamparnas Värld',
            'hero_title': 'Svamparnas Värld: Det Ultima Äventyret',
            'hero_subtitle': 'En resa in i det okända, där biologi möter gudomlighet.',
            'event_date': '2025-12-24',
            'about_text': 'Följ med på en unik resa genom mycelium-nätverket.',
        }

        for key, value in settings_data.items():
            Setting.objects.update_or_create(key=key, defaults={'value': value})

        # 2. Speakers
        s1, _ = Speaker.objects.update_or_create(
            name='Dr. M. Myceliaceae',
            defaults={
                'role': 'Professor i Mykologisk Neurobiologi',
                'bio': 'Ledande expert på svampnätverkens bio-elektriska kommunikation.',
                'order': 1
            }
        )

        s2, _ = Speaker.objects.update_or_create(
            name='A. Amanita',
            defaults={
                'role': 'Ljuddesigner & Myko-musiker',
                'bio': 'Pionjär inom översättning av biologiska signaler till auditiv konst.',
                'order': 2
            }
        )

        # 3. Agenda
        AgendaItem.objects.update_or_create(
            time='09:00 - 10:00',
            defaults={
                'title': 'Välkomstceremoni & Mycelium-meditation',
                'description': 'En introduktion till svamparnas heliga värld.',
                'order': 1
            }
        )

        AgendaItem.objects.update_or_create(
            time='10:15 - 11:45',
            defaults={
                'title': 'Bio-elektrisk Kommunikation',
                'speaker': s1,
                'description': 'Hur svampar pratar med varandra och oss.',
                'order': 2
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded webinar data'))
