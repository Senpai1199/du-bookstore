from django.contrib import admin
from registrations.models import Book, College, UserProfile, Course, BookSet

# Register your models here.

admin.site.register(Book)
admin.site.register(College)
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(BookSet)