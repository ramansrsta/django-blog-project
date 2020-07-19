from django.urls import path
from .views import index_page_view,blog_view

app_name = 'blogs'
urlpatterns=[
    path('',index_page_view,name='index'),
    path('blog-details/',blog_view,name='blog'),
]
