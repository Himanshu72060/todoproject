from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoall/', views.todo_all),
    path('todoall/<int:pk>', views.todo_all),
]
