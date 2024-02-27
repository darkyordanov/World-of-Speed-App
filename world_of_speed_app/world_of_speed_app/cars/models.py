from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app.cars.validators import year_validator
from world_of_speed_app.profiles.models import Profile

class Car(models.Model):
    MAX_LENGTH_MODEL = 15
    MIN_LENGTH_MODEL = 1
    
    MIN_VALUE_YEAR = 1999
    MAX_VALUE_YEAR = 2030
    
    MIN_VALUE_PRICE = 1.0

    CAR_TYPES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other')
    ]

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_LENGTH_MODEL,
        validators=[
            MinLengthValidator(MIN_LENGTH_MODEL)
        ],
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        validators=(
            year_validator,
        ),
        blank=False,
        null=False,
    )
    
    image_url = models.URLField(
        unique=True,
        blank=False,
        null=False,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.',
        }
    )
    
    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_VALUE_PRICE),
        ),
        blank=False,
        null=False,
    )
    
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def clean(self):
        if not self.MIN_VALUE_YEAR <= self.year <= self.MAX_VALUE_YEAR:
            raise ValidationError('Year must be between 1999 and 2030!')
        
    def __str__(self):
        return self.model

