from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scholarships/', views.scholarships, name='shcolarships'),
    path('scholarships/details/<int:id>', views.details, name='details'),
    path('scholarships/details2/<int:id>', views.details2, name='details'),
    path('scholarships/details3/<int:id>', views.details3, name='details'),
    path('scholarships/details4/<int:id>', views.details4, name='details'),
    path('search/', views.search, name='search'),
]