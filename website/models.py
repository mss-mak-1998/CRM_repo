from django.db import models

# Create your models here.

#RECRODS ARE LEADS
class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) #This just creates a time stamp in real time for each new created entry
    
    # Display utility function (Only returns first name, last name and age IF we only
    # call the records variable from our view  in our frontend)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age }'
    

    
