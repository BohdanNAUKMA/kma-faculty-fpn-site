from django.db import migrations


INSERT_EXCHANGE_DATA = """
INSERT INTO faculty_exchangeprogram (university, languages, seats, deadline, description)
VALUES 
('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', 'Один із найпрестижніших університетів Центральної Європи з потужними лабораторіями природничих наук.'),
('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01', 'Провідний дослідницький університет Європи з інноваційними програмами в біомедицині та екології.'),
('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', 'Найстаріший університет Литви, відомий дослідженнями в галузі молекулярної біології та біохімії.'),
('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', 'Старовинний академічний осередок із сучасним кампусом точних і природничих дисциплін.'),
('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', 'Флагман вищої освіти Балтії з сильними англомовними магістерськими програмами та дослідженнями довкілля.'),
('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', 'Сучасний інноваційний кампус із передовою матеріально-технічною базою для біологів та хіміків.');
"""

REVERSE_EXCHANGE_DATA = """
DELETE FROM faculty_exchangeprogram 
WHERE university IN (
    'Uniwersytet Warszawski, Польща',
    'KU Leuven (Бельгія)',
    'Vilnius University, Литва',
    'Uniwersytet Jagielloński, Польща',
    'University of Tartu - Естонія',
    'Masaryk University, Чехія'
);
"""


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_exchangeprogram'),
    ]

    operations = [
        migrations.RunSQL(
            sql=INSERT_EXCHANGE_DATA,
            reverse_sql=REVERSE_EXCHANGE_DATA,
        ),
    ]