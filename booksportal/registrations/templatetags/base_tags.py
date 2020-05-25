from django import template

from registrations.models import Book

register = template.Library()

@register.simple_tag()
def total_count(user):
    count = 0
    try:
        books = Book.objects.filter(seller__auth_user=user)
        for book in books:
            count += book.interested_count
        return count
    except Book.DoesNotExist:
        return 0