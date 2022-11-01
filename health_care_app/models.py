from django.db import models


class Patient(models.Model):

    GENDER = (
        ('F', 'F'),
        ('M', 'M'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Patients(models.Model):

    GENDER = (
        ('F', 'F'),
        ('M', 'M'),
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# SUPPORT
OPTION = (
    ('It heppened to me', 'It heppened to me'),
    ('It was already like that', 'It was already like that'),
)

REASON = (
    ('Delete patient', 'Delete patient'),
    ('System problems', 'System problems'),
    ('Others', 'Others'),
)

SITUATION = (
    ('Done', 'Done'),
    ('Pending', 'Pending'),
)


class Call(models.Model):
    terms = models.BooleanField('You got this responsability')
    user = models.CharField(max_length=100)
    message = models.TextField()
    option = models.CharField(max_length=100, choices=OPTION)
    reason = models.CharField(max_length=100, choices=REASON)
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(
        max_length=100, null=True, choices=SITUATION, default='Pending')

    def __str__(self):
        return self.user
