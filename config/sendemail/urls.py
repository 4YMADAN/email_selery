from django.urls import path

from .views import FeedbackFormView, success_view

urlpatterns = [
    path('contact/success/', success_view, name='success'),
    path('contact/', FeedbackFormView.as_view(), name='contact'),

]