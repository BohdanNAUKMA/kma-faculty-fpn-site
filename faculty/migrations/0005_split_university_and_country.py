import re
from django.db import migrations


def parse_university_and_country(raw_text):
    text = raw_text.strip()
    
    match_parentheses = re.match(r'^(.*?)\s*\((.*?)\)$', text)
    if match_parentheses:
        return match_parentheses.group(1).strip(), match_parentheses.group(2).strip()
    if ' - ' in text:
        parts = text.split(' - ', 1)
        return parts[0].strip(), parts[1].strip()

    if ',' in text:
        parts = text.rsplit(',', 1)
        return parts[0].strip(), parts[1].strip()

    return text, ''


def split_forward(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
    for item in ExchangeProgram.objects.all():
        clean_university, country = parse_university_and_country(item.university)
        item.university = clean_university
        item.country = country
        item.save()


def split_backward(apps, schema_editor):

    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
    for item in ExchangeProgram.objects.all():
        if item.country:
            if item.country == 'Бельгія':
                item.university = f"{item.university} ({item.country})"
            elif item.country == 'Естонія':
                item.university = f"{item.university} - {item.country}"
            else:
                item.university = f"{item.university}, {item.country}"
            item.country = ""
            item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_add_country_field'),
    ]

    operations = [
        migrations.RunPython(
            code=split_forward,
            reverse_code=split_backward,
        ),
    ]