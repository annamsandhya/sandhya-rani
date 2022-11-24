from django.shortcuts import render

# Create your views here.
def amma(request):
    d={'a':200}
    return render(request,'jinja_print.html',context=d)