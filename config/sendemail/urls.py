from django.urls import path

from . import views
from .views import FeedbackFormView, success_view

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/success/', success_view, name='success'),
    path('contact/', FeedbackFormView.as_view(), name='contact'),

]