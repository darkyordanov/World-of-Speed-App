from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from world_of_speed_app.profiles.validators import username_validator

   
class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 3
    
    MAX_LENGTH_PASSWORD = 20
    
    MAX_LENGTH_FIRST_NAME = 25
    MAX_LENGTH_LAST_NAME = 25
    
    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_USERNAME),
            username_validator
        ),
        blank=False,
        null=False,
        error_messages={
            'min_length': "Username must be at least 3 chars long!"
        }
    )
    
    email = models.EmailField(
        blank=False,
        null=False,
    )
    
    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(21, message='The age cannot be below 21.'),
        ),
        blank=False,
        null=False,
    )
    
    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        blank=True,
        null=True,
    )
    
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        blank=True,
        null=True,
    )
    
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.username