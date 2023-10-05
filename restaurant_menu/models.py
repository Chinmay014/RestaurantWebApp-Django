from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters","Starters"),
    ("salads","Salads"),
    ("main_dishes","Main Dishes"),
    ("dessert","Desserts")
)

STATUS = (
    (0,"Unavailable"),
    (1,"Available")
)
# I changed 'item' to 'Item' AFTER generating database. Let us see if it creates any issues later on.
class Item(models.Model):
    meal = models.CharField(max_length=80,unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=80, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS,default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.meal
