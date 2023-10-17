from django.db import models
from Application.models import Customer, CustomerContact

class Ticket(models.Model):
    id  = models.AutoField(primary_key=True)
    creator = models.ForeignKey(Customer, on_delete=models.CASCADE)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    message = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return self.title



class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(max_length=1000)
    commented_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    belongs_to_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
