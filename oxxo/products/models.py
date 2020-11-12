from django.db import models

# Create your models here.
class Beer( models.Model ):
    brand = models.CharField( max_length = 50 )
    alcohol = models.DecimalField( max_digits = 4, decimal_places = 2 )
    milliliters = models.IntegerField()
    handcrafted = models.BooleanField()
    nacinalty = models.CharField( max_length = 50, blank = True, null =  True )
    created = models.DateTimeField( auto_now_add = True )
    edited = models.DateTimeField( auto_now = True )

    def __str__ ( self ):
        return self.brand

class Customer( models.Model ):
    name = models.TextField( default = "Guest" )
    lastName = models.TextField( default = "Guest" )
    phone =  models.TextField( default = "Guest" )
    created = models.DateTimeField( auto_now_add = True )
    edited = models.DateTimeField( auto_now = True )

    def __str__ ( self ):
        return self.brand

class Order( models.Model ):
    quantity = models.IntegerField( default = 1 )
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE
    )
    beer = models.ForeignKey(
        'Beer',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField( auto_now_add = True )
    edited = models.DateTimeField( auto_now = True )