from django.db import models

# Create your models here.
# makemigration = create changes and store in a file 
# migrate = apply the pending changes created by makemigration

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    