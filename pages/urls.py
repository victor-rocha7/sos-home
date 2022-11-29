from django.urls import path, include
from .views import Home, About, Categories, CategoryDetail
import accounts

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('categories/', Categories.as_view(), name="categories"),
    path('categories/<int:cat_id>', CategoryDetail, name="category-detail"),
]