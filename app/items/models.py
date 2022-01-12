from django.db import models

#Model Items: 
class Item(models.Model):
    name = models.CharField(max_length=200)                 #item name
    category_id = models.PositiveIntegerField()             #item category id
    stock = models.PositiveIntegerField()                   #item stock number
    barcode_num = models.PositiveIntegerField(unique=True)  #item barcode number
    seller = models.CharField(max_length=200)               #item seller name

    
    