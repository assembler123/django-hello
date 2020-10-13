from django.shortcuts import render, HttpResponse

# Create your views here.
def index(Request):
    return render(Request,"index.htm")

def about(Request):
    return render(Request,"about.htm")
