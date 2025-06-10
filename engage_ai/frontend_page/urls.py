from django.urls import path
from frontend_page.views import login_page,access_page,signup_page,chatbot_page,control_page,dashboard_page,calender_page,email_page,chatbot_reciever_page
urlpatterns = [
    path('', login_page,name = "login_page"),
    path('access/',access_page,name = 'access_page'),
    path('signup/',signup_page,name="signup_page"),
    path('chatbot/',chatbot_page,name="chatbot_page"),
    path('control/',control_page, name='control_page'),
    path('dashboard/',dashboard_page, name='dahsboard_page'),
    path('calender/',calender_page, name='calender_page'),
    path('email/',email_page, name="email_page"),
    path('chat_reciever/',chatbot_reciever_page, name='chatbot_reciever_page'),



]
