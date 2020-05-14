from django import template

from registrations.models import Course

register = template.Library()

@register.simple_tag()
def get_year_semester(book):

    ordinal_indicator = {
                            1 : 'st',
                            2 : 'nd',
                            3 : 'rd'
                         }

    year = book.year
    sem = book.semester

    if year < 4:
        year_string = str(year) + ordinal_indicator[year]
        semester_string = str(sem) + ordinal_indicator[sem]
        year_sem_string = '<span class="label bg-cyan">{} year</span> \
        <span class="label bg-cyan">{} semester</span>'.format(year_string, semester_string)
    else:
        year_sem_string = '<span class="label bg-cyan">Masters</span>'

    return year_sem_string

@register.simple_tag()
def get_courses():
    courses = Course.objects.all()
    return list(courses)
