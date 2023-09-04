from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WineSerializer
from .models import Wine
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

class WineView(viewsets.ModelViewSet):
    serializer_class = WineSerializer
    queryset = Wine.objects.all()
    
def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)