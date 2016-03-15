from django.db import models

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