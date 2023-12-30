from django.db import models

class Truck(models.Model):
    SHACMAN = 'SHACMAN'
    SITRAK = 'SITRAK'

    CHOICE_GROUP = {
        (SHACMAN, 'SHACMAN'),
        (SITRAK,'SITRAK')
    }
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,unique=True, db_index=True,verbose_name="URL")
    description = models.TextField()
    equipment = models.TextField()
    minidescription = models.TextField()
    truckmodel = models.CharField(max_length=20, choices=CHOICE_GROUP)
    img = models.ImageField(default='truck.png', upload_to='product_image')

    def __str__(self):
        return self.name