from django import template

from registrations.models import Course, College

register = template.Library()

@register.simple_tag()
def get_year_semester(book):

    ordinal_indicator = {
                            1 : '1st',
                            2 : '2nd',
                            3 : '3rd',
                            4 : '4th',
                            5 : '5th',
                            6 : '6th',
                            7 : 'Masters'
                         }

    sem = book.semester

    if sem < 7:
        sem_string = '<span class="label bg-cyan">{} semester</span>'.format(ordinal_indicator[sem])
    else:
        sem_string = '<span class="label bg-cyan">{}</span>'.format(ordinal_indicator[sem])

    return sem_string

@register.simple_tag()
def get_courses():
    courses = Course.objects.all()
    return list(courses)

@register.simple_tag()
def getcampus(book):

    campus_opts = {
                    'N' : '<span class="label bg-red" style="font-size:10px">North Campus</span>',
                    'S' : '<span class="label bg-green" style="font-size:10px">South Campus</span>',
                    'O' : '<span class="label bg-grey" style="font-size:10px">Off Campus</span>'
                }
    campus = campus_opts[book.seller.college.category]

    return campus
