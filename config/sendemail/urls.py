from django.urls import path

from .views import contact_view, success_view

urlpatterns = [
    path('success/', success_view, name='success'),
    path('contact/', contact_view, name='contact'),

]