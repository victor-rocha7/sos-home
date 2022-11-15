from django.urls import path
from .views import Home, About, Categories, CategoryDetail

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('categories/', Categories.as_view(), name="categories"),
    path('categories/<int:cat_id>', CategoryDetail, name="category-detail"),
]