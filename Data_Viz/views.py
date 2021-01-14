
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .datacode import posts, lineplot1, lineplot2, pie_india, statewise_pie, statewise_bar

# Create your views here.



def index(request):
    return render(request, "Data_Viz/index.html")



def data(request):
    rangy = [ i for i in range(1, 38)]
    context = {
        'posts':posts,
        'plot1':lineplot1,
        'plot2':lineplot2,
        'plot3':pie_india,
        'plot4':statewise_pie, 
        'plot5':statewise_bar,
        'rangy':rangy
    }
    return render(request, "Data_Viz/data.html", context)



def about(request):
    return render(request, "Data_Viz/about.html")
    




def contact(request):
    # print(request.GET['y_name'])


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afterform')
    else:
        form = ContactForm()
        

    return render(request, "Data_Viz/contact.html", {'form':form})



def afterform(request):
    return render(request, "Data_Viz/afterform.html")