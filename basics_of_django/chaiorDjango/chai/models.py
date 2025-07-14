from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


# one to many 


class chaiReview(models.Model):
    chai=models.ForeignKey(chaivarity,on_delete=models.CASCADE,related_name='reviews')
    User=models.ForeignKey(User,on_delete=models.CASCADE,)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return f'{self.user.username} reveiw for {self.chai.name}'
    
#many to many

class Store(models.Model):
    Name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varieties=models.ManyToManyField(chaivarity,related_name='stores')

    def __str__(self):
        return self.Name
    

#one to one 

class chaiCertificate(models.Model):
    chai=models.OneToOneField(chaivarity,on_delete=models.CASCADE,related_name='chaicertificate')
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField()

    def __str__(self):
         return f'certificate for{self.name.chai}'     