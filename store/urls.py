
from django.urls import path

from . import views

urlpatterns = [


    # Store page

    path('store', views.store, name='store'),

    # Main page

    path('', views.home, name='home'),

    # Tour page

    path('tour', views.tour, name='tour'),


    # Music page

    path('music', views.music, name='music'),


    # Individual product

    path('product/<slug:product_slug>/', views.product_info, name='product-info'),


    # Individual category

    path('search/<slug:category_slug>/', views.list_category, name='list-category'),


]














