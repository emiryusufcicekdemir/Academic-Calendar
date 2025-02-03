from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Takvim adı

    def __str__(self):
        return self.name

class Event(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='events')  # Takvim ilişkisi
    name = models.CharField(max_length=100)  # Olay adı
    start_date = models.DateTimeField()  # Başlangıç tarihi
    end_date = models.DateTimeField()  # Bitiş tarihi

    def __str__(self):
        return self.name
