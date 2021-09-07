from django.urls import path
from .views import (HomePV, BlogDetailV, 
	BlogCreateV, BlogUpdateV, BlogDeleteV)

urlpatterns = [

    path('',  HomePV.as_view(), name = 'home'),
    path('post/<int:pk>', BlogDetailV.as_view(), name = 'detail'),
    path('post/new', BlogCreateV.as_view(), name = 'post_new'),
    path('post/edit/<int:pk>', BlogUpdateV.as_view(), name = 'post_edit'),
    path('post/delete/<int:pk>', BlogDeleteV.as_view(), name = 'post_delete')

]
