from django.db import models


class TVShow(models.Model):
    GENRES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Comedy', 'Comedy'),
        ('Documentary', 'Documentary'),
        ('Fantasy', 'Fantasy'),
        ('Drama', 'Drama'),
        ('Sports', 'Sports'),
        ('Musical', 'Musical'),
        ('Biography', 'Biography'),
        ('Education', 'Education')
    )
    title = models.CharField(max_length=50, verbose_name='name of the TV show')
    image = models.URLField(verbose_name='link to the image')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50, choices=GENRES, verbose_name='choose a genre')

    def __str__(self):
        return f'{self.title}-{self.genre}'
