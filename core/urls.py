
from django.contrib import admin
from django.urls import path, include
from api import views
from helloapi import views
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('blog.urls', namespace='blog')),
    # path('api/', include('blog_api.urls', namespace='blog_api')),
    # path('stuinfo/<int:pk>', views.student_detail),
    # path('stuinfo/', views.student_list),

    # path('stucreate/', views.student_create),
    path('productapi/', views.product_api)
]
