from django.shortcuts import render
"""
# Create your views here.
def post_list(request):
        return render(request, 'templates/adopcion/index.html', {})
"""

def home(request):
    return render(request, 'adopcion/home.html')
