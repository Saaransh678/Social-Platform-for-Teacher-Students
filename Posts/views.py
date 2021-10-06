from django.http import response
from django.shortcuts import render
from .models import Posts
from django.http import JsonResponse
# Create your views here.
def Home_View(request):
    return render(request, 'Pages/Home_Page.html', context={}, status=200)
def post_list_view(request):
    qs=Posts.objects.all()
    posts_list = [{"id":x.id,"content":x.content} for x in qs]
    data = {"response":posts_list}
    return JsonResponse(data)