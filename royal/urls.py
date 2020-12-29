from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("carmodel/", views.carmodel, name="carmodel"),
    path("carmodel-details/", views.carmodel_details, name="carmodel-details"),
    path("customisation/", views.customisation, name="Customisation"),
    path("testdrive/", views.testdrive, name="testdrive"),
    path("testdrive/success/", views.testdrivesuccess, name="testdrivesuccess"),
    path("logout/", views.logout, name="logout"),

]
