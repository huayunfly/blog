from django.db import models

# Create your models here.


class Blog(models.Model):
    """
    Blog model
    """
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    Author model
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    """
    Entry model
    """
    blog = models.ForeignKey(Blog, on_delete=True)
    headline = models.CharField(max_length=250)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline









