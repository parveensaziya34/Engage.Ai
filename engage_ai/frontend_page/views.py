from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'login_screen.html',{})

def signup_page(request):
    if request.method == 'POST':
        print(request.POST)
        print('form has been submitted')
        form_name=request.POST["name"]               
        form_email=request.POST["email"]
        form_pass=request.POST["password"]
        form_confirmpass=request.POST["confirm_password"]
        print(form_name)
        print(form_email)
        print(form_pass)
        print(form_confirmpass)
        if form_pass == form_confirmpass:
            print('pass is matched')
        else:
            print('pass is not matched')


    return render(request,'signup.html',{})


def dashboard_page(request):
    return render(request,'dashboard.html',{})

def access_page(request):
    return render(request,'access_matrix_admin.html',{})

def chatbot_page(request):
        return render(request,'chatbot.html',{})


