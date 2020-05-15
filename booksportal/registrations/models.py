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
    year = models.SmallIntegerField(default=1) # college year of the user

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
        Book can be of 2 types: Full Book / Reading (Each can contain/not contain notes)
        All masters books are to be put in 1 category. (Year - 4, Semester - 7). No further segregation required.
    """

    BOOK_TYPES = (
        ('B', 'Book'),
        ('R', 'Reading')
    )

    title = models.CharField(max_length=200, null=True)
    edition = models.CharField(max_length=200, blank=True)
    additional_details = models.CharField(max_length=200, blank=True)
    category = models.CharField(choices=BOOK_TYPES, null=False, max_length=1, default='R')
    contains_notes = models.BooleanField(default=False)
    condition = models.CharField(max_length=300, blank=False)
    year = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(4)]) # 4 for masters
    semester = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(2)]) # 0 for masters
    image = models.ImageField(upload_to='book_pics', null=False)
    course = models.ForeignKey('Course', related_name='course_books', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    sold = models.BooleanField(default=False)
    interested_count = models.SmallIntegerField(default=0)
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    seller = models.ForeignKey("UserProfile", related_name="seller_books", on_delete=models.CASCADE)
    bookset = models.ForeignKey('BookSet', related_name='set_books', null=True,
        blank=True, on_delete=models.CASCADE)

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
        Handles college data (to be populated using script)
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

class Course(models.Model):
    """
        Handles Course data (to be populated using sheet).
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class BookSet(models.Model):
    """
        Used for selling a set of related books.
        Contains Information about price, course, etc.
    """
    title = models.CharField(max_length=200, null=True)
    additional_details = models.CharField(max_length=200, blank=True)
    course = models.ForeignKey('Course', related_name='course_bookset',
        on_delete=models.CASCADE)
    year = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(4)]) # 4 for master
    semester = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(2)]) # 0 for masters
    price = models.IntegerField(default=0)
    sold = models.BooleanField(default=False)
    contains_books = models.BooleanField(default=False)
    contains_notes = models.BooleanField(default=False)
    contains_readings = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.id, self.title)
