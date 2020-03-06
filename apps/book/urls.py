from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('books/', views.MovieBookListView.as_view(), name='books'), # 图书列表

    path('book_list/<int:pk>', views.BookListView.as_view(), name='book_list'),

]