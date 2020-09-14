from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .utils import unique_slug_generator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pics/wallpaper_23.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Product(models.Model):
    Status = [('Available', 'Available'), ('Out of Stock', 'Out of Stock')]
    Catagory = [('Food', 'Food'), ('Wear','Wear'), ('Shoes', 'Shoes'), ('Electronic', 'Electronic'), ('Mobile', 'Mobile'), ('Book', 'Book'), ('Utilities', 'Utilities'), ('Other', 'Other')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    catagory = models.CharField(choices=Catagory, max_length=50)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    descrip = models.CharField(max_length=400)
    status = models.CharField(max_length=20, choices=Status)
    item_image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.item_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.item_image.path)




def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
	    instance.slug = unique_slug_generator(instance) 


pre_save.connect(pre_save_receiver, sender = Product) 