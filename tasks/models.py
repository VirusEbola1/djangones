from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    release_date = models.DateField()
    rom_file = models.FileField(upload_to='dendy/') 

    def __str__(self):
        return self.title