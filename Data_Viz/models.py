from django.db import models

# Create your models here.

class SendMsg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    message = models.TextField(blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.email, self.message, self.time