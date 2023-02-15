from rest_framework.authtoken import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', Quiz.as_view(), name='quizzes'),
    path('random/<str:topic>', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>', QuizQuestion.as_view(), name='quiz-questions'),
    
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]

