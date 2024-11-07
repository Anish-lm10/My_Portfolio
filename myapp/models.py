from django.db import models

# Create your models here.
class Education(models.Model):
    subject=models.CharField(max_length=255)
    college_institute_year=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.subject
    

class Works(models.Model):
    image=models.ImageField(upload_to='image')
    work_title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self) -> str:
        return self.work_title





