from django.db import models
from django.utils import timezone

# Create your models here.
class chaivarity(models.Model):
    CHAI_TYPE_CHOICE=[
        ('masala', 'Masala Chai'),
        ('tulsi', 'Tulsi Chai'),
        ('adrak', 'Adrak Chai'),
        ('elaichi', 'Elaichi Chai'),
        ('lemongrass', 'Lemongrass Chai'),
    ]


    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=50, choices=CHAI_TYPE_CHOICE )
    description = models.TextField(default='')








    def __str__(self):
        return self.name