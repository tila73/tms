from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    employee = models.CharField(max_length=100)
    task_desc = models.TextField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    image = models.ImageField(upload_to='img/', blank=False)

    def __str__(self):
        return str(self.task_name)
