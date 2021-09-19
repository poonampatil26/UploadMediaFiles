from django.db import models

# Create your models here.

brand_choices = [
    ('redmi', 'Redmi'),
    ('samsung','Samsung'),
    ('apple', 'Apple'),
    ('oppo','Oppo'),
    ('vivo', 'Vivo'),
    ('realme','Realme')
]

sim_type_choices = [
    ('single sim', 'Single Sim'),
    ('dual sim','Dual Sim')
]

class Mobile(models.Model):
    mobile_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, choices=brand_choices)
    ram = models.IntegerField()
    price = models.FloatField()
    internal_storage = models.IntegerField()
    battery_capacity = models.IntegerField()
    sim_type = models.CharField(max_length=50, choices=sim_type_choices)
    image = models.FileField(upload_to='document/')


    def __str__(self):
        return self.mobile_name