from django.urls import path
from .views import criterion_create , criterion_delete , criterion_update , home , test

urlpatterns = [
    path('test/' , test , name='test'),
    path('criteria/', home, name='home'),
    path('criteria/new/', criterion_create, name='criterion_create'),
    path('criteria/<int:pk>/edit/', criterion_update, name='criterion_update'),
    path('criteria/<int:pk>/delete/', criterion_delete, name='criterion_delete'),
]
