from django.db import models # importing models.py from Django DB , the actual github repo

# Create your models here.

class Item(models.Model):  #Think of this class as a single table  , now django automatically creates an item table , the parameter is inherting the model class from the model import above, remeber in this case we dont have to specify __init__ for example like flask.
    name = models.CharField(max_length=50, null=False , blank =False) # blank makes it required on forms.
    done = models.BooleanField(null=False , blank =False ,default= False) # use makemigrations command to make the file

    def __str__(self): # This is so that we can see the item object names in the admin panel
        return self.name

