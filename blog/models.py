from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    blog_content = models.CharField(max_length=120)
    authorName = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.blog_content