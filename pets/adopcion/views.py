from django.shortcuts import render
"""
# Create your views here.
def post_list(request):
        return render(request, 'templates/adopcion/index.html', {})
"""
def index(request):
    return render(request, 'adopcion/index.html')