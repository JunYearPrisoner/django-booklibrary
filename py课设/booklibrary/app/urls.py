from django.urls import path
from app import views

urlpatterns = [
    path('addbook/', views.addbook),
    path('booklist/', views.booklist),
    path('edit_book/', views.edit_book),
    path('del_book/', views.del_book),
    path('find/', views.find),
    path('find_end/', views.find_end),

]
