from django.db import models

class Post(models.Model):
    ism = models.CharField(max_length=255)
    malumot = models.TextField()
    tanlov = models.CharField(max_length=20)
    malumot = models.DateTimeField(auto_now_add=True)
    rasm = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.ism

class TopPost(models.Model):

    ism = models.CharField(max_length=255)
    tanlov = models.CharField(max_length=20)
    malumot = models.DateTimeField(auto_now_add=True)
    rasm = models.CharField(max_length=255) 

    def __str__(self) -> str:
        return self.ism

class Top(models.Model):
    ism = models.CharField(max_length=255)
    tanlov = models.CharField(max_length=20)
    malumot = models.DateTimeField(auto_now_add=True)
    rasm = models.CharField(max_length=255) 

    def __str__(self) -> str:
        return self.ism