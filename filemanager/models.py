from django.db import models


# Create your models here.

# def user_directory_path(instance, filename):
#    return '{0}/{1}'.format(instance.author, filename)


class Files(models.Model):
    comment = models.CharField(max_length=50, default='No Comments')
    file = models.FileField(upload_to='userData/')

    def __str__(self):
        return self.file.name
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)