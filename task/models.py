from django.db import models

class Task(models.Model):
    title = models.TextField(
        verbose_name="Название"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Status(models.TextChoices):
        TODO = 'todo', "Не выполнено"
        IN_PROGRESS = "in_progress", "В процессе"
        DONE = "done", "Выполнена"

    status = models.TextField(
        choices=Status.choices,
        default=Status.TODO,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        return self.title