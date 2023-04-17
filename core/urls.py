from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('post/<int:post_id>', post, name="post"),
    path('category/<int:category_id>', category, name="category"),
    path('author/<int:author_id>', author, name="author"),
    path('dates/<int:month_id>/<int:year_id>', dates, name="dates"),
]


