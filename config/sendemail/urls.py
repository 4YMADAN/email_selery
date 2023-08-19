from django.urls import path

from .views import FeedbackFormView, SuccessView

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('contact/', FeedbackFormView.as_view(), name='contact'),

]