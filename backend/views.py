from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Police Checkpoint API. Use /api/auth/ for endpoints.")