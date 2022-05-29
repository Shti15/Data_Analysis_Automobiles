from urllib import response
from django.shortcuts import render, HttpResponse
import data_processing.Data_visualization as Dv
from data_processing.custom_query import start_chat
# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def visualize(request):
    if request.method == 'POST':
        id= request.POST.get('id')
        chart=Dv.visualization(id) 
        return render(request, 'visual.html',{'chart':chart})

def custom_query(request):
    if request.method=="GET":
        return render(request,"custom_query.html")
    if request.method=="POST":
        search_query = request.POST.get('query')
        bot_response = start_chat(search_query)
        print(search_query)
        context = {
          'bot_res' : bot_response,
          'query_val': search_query,  
        }
        return render(request,"custom_query.html",context)

def visual_4w(request):
    if request.method=="GET":
        return render(request,"visual_4w.html")

def visual_ev(request):
    if request.method=="GET":
        return render(request,"visual_ev.html")

