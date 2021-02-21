from django.db import models

# Create your models here.
class customer(models.Model):
    name= models.CharField(max_length=200,null=False)
    email= models.CharField(max_length=200)
    balance = models.IntegerField(default="100")

    def __str__(self):
        
        return '{}  {}  {}'.format(self.name, self.email,self.balance)


class transfer(models.Model):
   
    fromName = models.CharField(max_length=200, null=False, default="null")
    toName =models.CharField(max_length=200,null=False,default="null")
    amount=models.IntegerField(null=False)

    def __str__(self):
        return '{}  {}  {} {}  {}'.format(self.toC, self.fromName,self.toName,self.amount,self.fromC)
    
