import re
from django.db import migrations


def clean_seats_forward(apps, schema_editor):

    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
    for item in ExchangeProgram.objects.all():
        raw_seats = str(item.seats).strip()
        match = re.search(r'\d+', raw_seats)
        if match:
            item.seats = match.group(0)
            item.save()


def clean_seats_backward(apps, schema_editor):

    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
    for item in ExchangeProgram.objects.all():
        item.seats = str(item.seats)
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0005_split_university_and_country'),
    ]

    operations = [
        migrations.RunPython(
            code=clean_seats_forward,
            reverse_code=clean_seats_backward,
        ),
    ]