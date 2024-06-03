from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('news/list/', NewsListView.as_view(), name='news'),
    path('news/detail/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('teacher/detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    path('cafedra/list/', CafedraListView.as_view(), name='cafedras'),
    path('cafedra/detail/<int:pk>/', CafedraDetailView.as_view(), name='cafedra_detail'),
    path('page/detail/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('contact/', ApplicationCreateView.as_view(), name='contact'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
]
