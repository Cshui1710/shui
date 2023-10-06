from django.db import models

# Create your models here.

class Topics(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creted_by = models.ForeignKey('auth.User', related_name='topics', on_delete=models.CASCADE)

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)