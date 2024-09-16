from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('qpaper', views.qpaper, name='qpaper'),
    path('notes', views.notes, name='notes'),
    path('books', views.books, name='books'),
    path('about', views.about, name='about'),
    path('policy', views.policy, name='policy'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('contactinfo', views.contactinfo, name='contactinfo'),
    path('delete_contact_entry/<int:entry_id>/', views.delete_contact_entry, name='delete_contact_entry'),
    path('gallery', views.gallery, name='gallery'),
]