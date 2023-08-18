from django.contrib import admin
from django.urls import path
from library import views
from library.views import custom_404

handler404 = custom_404

urlpatterns = [
    path("", views.all_books, name="all_books"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'), 
    path("<int:book_id>/", views.single_book, name="single_book"),
    path('search_books/', views.search_book, name='search_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<int:book_id>/remove/', views.remove_book, name='remove_book'),
    path('book/<int:book_id>/update/', views.update_book, name='update_book'),
    path('my_loans/', views.my_loans, name='my_loans'),
    path('loan/<int:book_id>/', views.loan_book, name='loan_book'),
    path('contact/', views.contact, name='contact'),

   
]
