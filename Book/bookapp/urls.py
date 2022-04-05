from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('registration', registration),
    path('login', loginFunction),
    path('student',studentDashboard),
    path('adm',adminDashboard),
    path('update/<int:id>', updateBook),
    path('delete/<int:id>', deleteBook)

]