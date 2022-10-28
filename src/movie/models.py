from django.db import models
from django.utils.text import slugify

# Create your models here.

class MovieType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Logic
        self.slug = slugify(self.name) 
        super(MovieType,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Subtitle(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.URLField(max_length=250)
    
    def __str__(self):
        return self.name


class Actor(models.Model):
    def image_upload(instance, filename):
        image_name = slugify(instance.name)
        image_list = filename.split(".")
        extension = image_list[len(image_list)-1]
        return "static/images/actors/%s.%s"%(image_name, extension)
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload, max_length=255)
    wikipedia_url = models.URLField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Logic
        self.slug = slugify(self.name) 
        super(Actor,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    


class Movie(models.Model):
    country_choice = (
        ('US', 'US'),
        ('UK', 'UK'),
        ('Canada', 'Canada'),
        ('Japan', 'Jaban'),
        ('Kore', 'Kore'),
        ('Turkey', 'Turkey'),
    )
    movie_language = (
        ('en', 'English'),
        ('fr', 'Frensh'),
        ('sp', 'Spanish'),
        ('ar', 'Arabic'),
        ('tr', 'Turkish'),
        ('gr', 'German'), 
        ('it', 'Italian')
    )
    def image_upload(instance, filename):
        image_list = filename.split(".")
        extension = image_list[len(image_list)-1]
        return "static/images/movies/%s.%s"%(instance.slug, extension)
    
    name = models.CharField(max_length=100)
    type = models.ManyToManyField(MovieType, related_name='movie_type', blank=True)
    description = models.TextField(max_length=500)
    country = models.CharField(max_length=50, choices=country_choice)
    running_time = models.IntegerField()
    published_at = models.DateField(auto_now=True)
    released = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=image_upload, max_length=255)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    producer = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    trailer = models.URLField(max_length=250)
    language = models.CharField(max_length=25, choices=movie_language)
    subtitle = models.OneToOneField(Subtitle, on_delete=models.SET_NULL, null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movie_actors', blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Logic
        self.slug = slugify(self.name) 
        super(Movie,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Series(models.Model):
    country_choice = (
        ('US', 'US'),
        ('UK', 'UK'),
        ('Canada', 'Canada'),
        ('Japan', 'Jaban'),
        ('Kore', 'Kore'),
        ('Turkey', 'Turkey'),
    )
    series_language = (
        ('en', 'English'),
        ('fr', 'Frensh'),
        ('sp', 'Spanish'),
        ('ar', 'Arabic'),
        ('tr', 'Turkish'),
        ('gr', 'German'), 
        ('it', 'Italian')
    )
    def image_upload(instance, filename):
        image_name = slugify(instance.name)
        image_list = filename.split(".")
        extension = image_list[len(image_list)-1]
        return "static/images/series/%s.%s"%(image_name, extension)
    
    name = models.CharField(max_length=150)
    type = models.ManyToManyField(MovieType, related_name='series_type', blank=True)
    description = models.TextField(max_length=500)
    country = models.CharField(max_length=50, choices=country_choice)
    image = models.ImageField(upload_to=image_upload, max_length=255)
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    season_count = models.IntegerField()
    epsoide_count = models.IntegerField()
    producer = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    language = models.CharField(max_length=25, choices=series_language)
    actors = models.ManyToManyField(Actor, related_name='series_actors', blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Logic
        self.slug = slugify(self.name) 
        super(Series,self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=100)
    epsoide_count = models.IntegerField()
    production_date = models.DateField()
    trailer = models.URLField(max_length=255)
    series = models.ForeignKey(Series, related_name='Series', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Logic
        self.slug = slugify(self.name) 
        super(Season,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name 


class Epsoide(models.Model):
    name = models.CharField(max_length=150)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    season = models.ForeignKey(Season, related_name='season', on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    subtitle = models.ForeignKey(Subtitle, related_name='epsoide_subtitle', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        # Logic
        self.slug = slugify(self.name) 
        super(Epsoide,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name