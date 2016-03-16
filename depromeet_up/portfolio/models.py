from django.db import models
import uuid

# Create your models here.
class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class board(models.Model):
    post_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.post_id)

class imghandler(models.Model):

    upload_path = '/home/ec2-user/depromeet_up/deploy_static/media/image'
    image = models.ImageField(upload_to='/static/media/image', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    post_id = models.ForeignKey(board, on_delete=models.CASCADE, related_name='imgs')

    def save(self, *args, **kwargs):
        if self.image_url:
            import urllib, os
            from urlparse import urlparse

            file_save_dir = self.upload_path
            filename = str(uuid.uuid4())
            urllib.urlretrieve(self.image_url, os.path.join(file_save_dir, filename))
            self.image = os.path.join('/static/media/image', filename)
            self.image_url = ''
        super(imghandler, self).save()