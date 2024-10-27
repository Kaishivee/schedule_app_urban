from django.db import models


class Group(models.Model):
    name = models.CharField("Название группы", max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    DAYS_OF_WEEK = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
    ]

    name = models.CharField("Название урока", max_length=100)
    date = models.DateField("Дата")
    time = models.TimeField("Время")
    classroom = models.CharField("Аудитория", max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    day_of_week = models.CharField(
        "День недели",
        max_length=11,
        choices=DAYS_OF_WEEK
    )

    def __str__(self):
        return f"{self.name} - {self.group.name} ({self.day_of_week})"
