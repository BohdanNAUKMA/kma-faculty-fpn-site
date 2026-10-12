from django.db import models

# Create your models here.
class Department(models.Model):
    """Кафедра Факультету природничих наук (ФПрН)"""
    name = models.CharField (
        max_length=255,
        verbose_name="Назва кафедри",
        help_text="Наприклад: Кафедра хімії, Кафедра біології, Кафедра екології"
    )
    head_name = models.CharField (
        max_length=255,
        verbose_name="Завідувач кафедри",
        help_text="ПІБ та наукове звання завідувача кафедри"
    )

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):
    """Освітня програма / Спеціальність ФПрН"""
    name = models.CharField (
        max_length=255,
        verbose_name="Назва спеціальності",
        help_text="Наприклад: Хімія, Біологія, Екологія, Фізика"
    )
    code = models.CharField (
        max_length=50,
        verbose_name="Код спеціальності",
        help_text="Наприклад: 102 (Хімія), 091 (Біологія), 101 (Екологія)"
    )
    description = models.TextField (
        verbose_name="Повний опис спеціальності",
        help_text="Детальний опис програми (перші 50 слів відображатимуться у загальному списку)"
    )
    coordinator_name = models.CharField (
        max_length=255,
        verbose_name="Імʼя координатора набору (гаранта програми)"
    )
    coordinator_contact = models.CharField (
        max_length=255,
        verbose_name="Контакт координатора",
        help_text="Корпоративний email (@ukma.edu.ua) або телефон"
    )
    department = models.ForeignKey (
        Department,
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="Випускова кафедра"
    )
    disciplines = models.TextField(
        verbose_name="Список дисциплін",
        help_text="Перелік ключових дисциплін (кожна з нового рядка або через кому)"
    )

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    """Викладач ФПрН"""
    name = models.CharField (
        max_length=255,
        verbose_name="Імʼя викладача"
    )
    position = models.CharField (
        max_length=255,
        verbose_name="Посада",
        help_text="Наприклад: професор, доцент, старший викладач"
    )
    degree = models.CharField (
        max_length=255,
        verbose_name="Науковий ступінь",
        help_text="Наприклад: д-р хім. наук, канд. біол. наук, PhD"
    )
    department = models.ForeignKey (
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Кафедра"
    )

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.position})"


class FacultyInfo(models.Model):
    """Інформація для головної сторінки ФПрН (Singleton-підхід)"""
    title = models.CharField (
        max_length=255,
        default="Факультет природничих наук НаУКМА",
        verbose_name="Заголовок факультету"
    )
    description = models.TextField (
        verbose_name="Опис факультету",
        help_text="Загальна інформація про місію, історію та наукову діяльність ФПрН"
    )
    contacts = models.TextField (
        verbose_name="Контакти деканату",
        help_text="Адреса (корпус, кімната), телефони, робочі години та пошта деканату"
    )

    class Meta:
        verbose_name = "Інформація про факультет"
        verbose_name_plural = "Інформація про факультет (Головна сторінка)"

    def __str__(self):
        return self.title