from django.urls import path
from .views import chatbot_api,chat_ui

urlpatterns = [
    path('chat/', chatbot_api),
     path('ui/', chat_ui),
]