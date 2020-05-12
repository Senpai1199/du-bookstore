from django.db import models

from django.contrib.auth.models import User

from PIL import Image

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class UserProfile(models.Model):
    """
        Handles the buyers/sellers registering on the portal.
    """
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    gender = models.CharField(choices=GENDERS, null=True, max_length=1)
    auth_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, unique=True, related_name="profile")
    college = models.ForeignKey("College", on_delete=models.CASCADE, null=False)
    image = models.ImageField(default="default_male_dp.jpeg", upload_to='profile_pics', null=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return "{} - {}".format(self.id, self.auth_user.first_name)

class Book(models.Model):
    """
        Contains info of a full book/compiled 'Reading'
        All masters books are to be put in 1 category. (Year - 4, Semester - 7). No further segregation required.
    """
    title = models.CharField(max_length=200, blank=False)
    condition = models.CharField(max_length=300, blank=False)
    year = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(4)]) # 4 for master
    semester = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(7)]) # 7 for masters
    image = models.ImageField(upload_to='book_pics', null=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return "{} - {}".format(self.id, self.title)

class College(models.Model):
    """
        Handles college data (to be populated by parsing an excel sheet)
    """
    COLLEGE_TYPES = (
        ('N', 'North Campus'),
        ('S', 'South Campus'),
        ('O', 'Off Campus')
    )

    name = models.CharField(max_length=200, blank=False)
    category = models.CharField(choices=COLLEGE_TYPES, null=False, max_length=1, default='S')

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

