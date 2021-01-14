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





def msg_for_admins(request):
    # If not loged in then redirect to login page. Once logged in redirect to msg page.
    return render(request, "Data_Viz/msg.html")