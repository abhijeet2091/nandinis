from django.db import models
#from django.contrib.auth.models import User
from members.models import User
from django.utils import timezone

class Sweet(models.Model):
    sweet_category = models.CharField(max_length=100)
    sweet_name = models.CharField(max_length=100, primary_key=True)
    price = models.IntegerField(default=100)

    def __str__(self): 
        return self.sweet_name
    
class Order(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    order_quan = models.FloatField(default=0.0)
    sweet_name = models.ForeignKey(Sweet, on_delete=models.CASCADE)
    order_val = models.FloatField(default=0.0)
    order_dt_crt = models.DateTimeField(editable=False)
    order_dt_mod = models.DateTimeField()
    order_id = models.IntegerField()
    order_delivered = models.BooleanField(default=False)
    order_confirmed = models.BooleanField(default=False)

   
    def __str__(self):
        return str(self.email)
    
    #Overriding the save method
    def save(self, *args, **kwargs):
        # On save, update timestamps
        #if not self.order_id:
        self.order_dt_crt = timezone.now()
        self.order_dt_mod = timezone.now()
        return super(Order, self).save(*args, **kwargs)