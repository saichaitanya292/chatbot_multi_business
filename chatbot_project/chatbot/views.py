from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_bot_response

@api_view(['GET','POST'])
def chatbot_api(request):
    user_message = request.data.get('message', '')
    bot_reply = get_bot_response(user_message)

    return Response({
        "user": user_message,
        "bot": bot_reply
    })


def chat_ui(request):
    return render(request, 'chatbot/chat.html')