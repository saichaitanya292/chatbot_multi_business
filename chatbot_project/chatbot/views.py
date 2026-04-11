from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .utils import get_bot_response

@api_view(['GET','POST'])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def chatbot_api(request, business_name=None):
    user_message = request.data.get('message', '')
    bot_reply = get_bot_response(user_message, business_name)

    return Response({
        "user": user_message,
        "bot": bot_reply
    })


def chat_ui(request):
    return render(request, 'chatbot/chat.html')