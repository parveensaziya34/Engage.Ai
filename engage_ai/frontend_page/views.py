from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'login_screen.html',{})


def dashboard_page(request):
    return render(request,'dashboard.html',{})

def access_page(request):
    return render(request,'access_matrix_admin.html',{})
