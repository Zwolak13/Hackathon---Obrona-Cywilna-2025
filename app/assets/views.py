from django.shortcuts import render

def home(request):
    """Home view for the assets app."""
    return render(request, 'pages/home.html') 