from django.urls import path
from nuevaapp import views

urlpatterns = [
    path('tips/', views.tipsListView.as_view(), name='tips'),
    path('tips/create', views.tipsCreateView.as_view(), name='create_tips'),
    path('tips/<int:pk>/detail', views.tipsDetailView.as_view(), name='detail_tips'),
    path('tips/<int:pk>/update', views.tipsUpdateView.as_view(), name='update_tips'),
    path('tips/<int:pk>/delete', views.tipsDeleteView.as_view(), name='delete_tips'),
]
