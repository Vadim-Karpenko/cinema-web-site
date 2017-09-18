from django.db import models
from sorl.thumbnail import ImageField
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode


class Movie(models.Model):
    GENRE_CHOICES = (
        ('comedy', 'Comedy'),
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('crime', 'Crime'),
        ('drama', 'Drama'),
    )

    title = models.CharField(max_length=100, unique=True)
    image = ImageField(upload_to='movies/%Y/%m/%d')
    description = models.TextField()
    slug = models.SlugField(help_text="A short label, generally used in URLs.", unique=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=40)
    duration = models.PositiveSmallIntegerField(help_text="Film duration, in minutes.")
    price = models.PositiveSmallIntegerField(help_text="Price of one ticket, in dollars.")
    start_time = models.DateTimeField(help_text="When film will be show in cinema.")
    release_date = models.DateField(help_text="When film was releaded.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Movie, self).save(*args, **kwargs)

class Places(models.Model):
    chain_models = models.OneToOneField(Movie, on_delete=models.CASCADE)

    row1_place1 = models.BooleanField(default=False)
    row1_place2 = models.BooleanField(default=False)
    row1_place3 = models.BooleanField(default=False)
    row1_place4 = models.BooleanField(default=False)
    row1_place5 = models.BooleanField(default=False)
    row1_place6 = models.BooleanField(default=False)
    row1_place7 = models.BooleanField(default=False)
    row1_place8 = models.BooleanField(default=False)

    row2_place1 = models.BooleanField(default=False)
    row2_place2 = models.BooleanField(default=False)
    row2_place3 = models.BooleanField(default=False)
    row2_place4 = models.BooleanField(default=False)
    row2_place5 = models.BooleanField(default=False)
    row2_place6 = models.BooleanField(default=False)
    row2_place7 = models.BooleanField(default=False)
    row2_place8 = models.BooleanField(default=False)

    row3_place1 = models.BooleanField(default=False)
    row3_place2 = models.BooleanField(default=False)
    row3_place3 = models.BooleanField(default=False)
    row3_place4 = models.BooleanField(default=False)
    row3_place5 = models.BooleanField(default=False)
    row3_place6 = models.BooleanField(default=False)
    row3_place7 = models.BooleanField(default=False)
    row3_place8 = models.BooleanField(default=False)

    row4_place1 = models.BooleanField(default=False)
    row4_place2 = models.BooleanField(default=False)
    row4_place3 = models.BooleanField(default=False)
    row4_place4 = models.BooleanField(default=False)
    row4_place5 = models.BooleanField(default=False)
    row4_place6 = models.BooleanField(default=False)
    row4_place7 = models.BooleanField(default=False)
    row4_place8 = models.BooleanField(default=False)

    row5_place1 = models.BooleanField(default=False)
    row5_place2 = models.BooleanField(default=False)
    row5_place3 = models.BooleanField(default=False)
    row5_place4 = models.BooleanField(default=False)
    row5_place5 = models.BooleanField(default=False)
    row5_place6 = models.BooleanField(default=False)
    row5_place7 = models.BooleanField(default=False)
    row5_place8 = models.BooleanField(default=False)

    def __str__(self):
        return 'Places for ' + self.chain_models.title
