from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('about_game',views.about),
    path('download',views.download),
    path('sign_in',views.sign_in),
    path('sign_up',views.sign_up)
]
