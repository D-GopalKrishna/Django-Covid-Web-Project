from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, "Data_Viz/index.html")



def data(request):
    return render(request, "Data_Viz/data.html")




def about(request):
    return render(request, "Data_Viz/about.html")
    



def contact(request):
    return render(request, "Data_Viz/contact.html")
