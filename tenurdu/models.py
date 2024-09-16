from django.db import models

# Create your models here.
class Standard(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Youtube(models.Model):
    title = models.CharField(max_length=100, null=True)
    youtube_link = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title + '(' +  self.subject.name + ')'

class Qpaper(models.Model):
    title = models.CharField(max_length=100, null=True)
    qpaper = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    def __str__(self):
        return self.title + '(' +  self.subject.name + ')'

class Notes(models.Model):
    title = models.CharField(max_length=100, null=True)
    notes = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    def __str__(self):
        return self.title + '(' +  self.subject.name + ')'
    
class Books(models.Model):
    title = models.CharField(max_length=100, null=True)
    book_link = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    def __str__(self):
        return self.title + '(' +  self.subject.name + ')'
    
class Contactinfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.ImageField(upload_to='gallery_images/')