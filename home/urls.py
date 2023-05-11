from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sentry_error', views.sentry_error, name='sentry-error')
]
