"""booksportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registrations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # redirect to home
    path('base/', views.base_view, name='base'),

    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),

    path('home/', views.home, name='home'),
    path('sell_book/', views.sell_book, name='sell_book'),
    path('my_listings/', views.view_listings, name='my_listings'),
    path('my_set_listings/', views.view_set_listings, name='my_set_listings'),

    path('mark_sold/<int:b_id>/', views.mark_sold, name='mark_sold'),
    path('editing_listing_details/<int:b_id>/', views.edit_listing_details, name='edit_listing_details'),

    path('search_book/', views.search_book, name='search_book'),
    path('search_bookset/', views.search_bookset, name='search_bookset'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
