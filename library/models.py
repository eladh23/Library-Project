from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    city = models.CharField(max_length=100,null=True)
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.username
    
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.PositiveIntegerField()
    image = models.ImageField(upload_to='all_books/', null=True, blank=True)
    borrowers = models.ManyToManyField(CustomerUser, through='Loan')

class Loan(models.Model):
    LOAN_TYPES = (
        (1, 'up to 10 days'),
        (2, 'up to 5 days'),
        (3, 'up to 2 days'),
    )

    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)
    loan_type = models.IntegerField(choices=LOAN_TYPES, default=1)  

    def __str__(self):
        return f"{self.customer.username} borrowed {self.book.name} in {self.loan_date}"