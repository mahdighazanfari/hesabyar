from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.TextField(max_length=10,
                             unique=True,
                             help_text='Required. 10 characters without zero. digits only.',
                             error_messages={
                                 'unique': "A user with that phone already exists.",
                             }, )

    objects = UserManager()


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=None)
    amount = models.FloatField()
    category = models.IntegerField()


class TransactionMember(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=None)


class Contact(models.Model):
    user = models.ForeignKey(User, related_name='user_id', on_delete=None)
    contact = models.ForeignKey(User, related_name='contact_id', on_delete=None)
