from django.shortcuts import render
from django.http import JsonResponse
from .groq_handler import generate_sql_from_nl, execute_sql, generate_nl_response

# Create your views here.
def login_page(request):
    return render(request,'login_page.html',{})

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


    return render(request,'signup_page.html',{})


def dashboard_page(request):
    return render(request,'dashboard.html',{})

def access_page(request):
    return render(request,'access_matrix_admin.html',{})

def chatbot_page(request):
    if request.method == "POST":
        question = request.POST.get("question", "")
        try:
            sql_query = generate_sql_from_nl(question)
            sql_result = execute_sql(sql_query)
            nl_response = generate_nl_response(question, sql_result)
            return JsonResponse({"response": nl_response})
        except Exception as e:
            return JsonResponse({"response": f"Error: {str(e)}"}, status=500)
    return render(request, 'chatbot.html', {})


def control_page(request):
        return render(request,'control_policy_admin.html',{})

def calender_page(request):
     return render(request,'calender.html',{})

def email_page(request):
     return render(request,'email_template.html',{})

def chatbot_reciever_page(request):
     return render(request,'chatbot_reciever.html', {})