from django.db import models

# Create your models here.
class User(models.Model):

    #id = models.CharField()
    name = models.CharField(max_length=250,null=False)
    email = models.CharField(max_length=250,null=False)
    def __str__(self):
        return self.name

class Restaurant(models.Model):

    #id = models.CharField()
    name = models.CharField(max_length=250,null=False)
    user_id = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=80,null=False)
    description = models.CharField(max_length=250,null=False)
    price = models.IntegerField(null=False)
    course = models.CharField(max_length=100,null=True)
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    #restaurant = relationship(Restaurant)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    #user = relationship(User)
    def __str__(self):
        return [self.name, self.description, self.price, self.course, self.restaurant_id]



