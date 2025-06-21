from django.urls import path
from frontend_page.views import login_page,access_page,signup_page,chatbot_page, dashboard_page, logout_user,calender_page, control_page
urlpatterns = [
    path('', login_page,name = "login_page"),
<<<<<<< HEAD
    path('signup/', signup_page, name='signup_page'),
=======
    path('access/',access_page,name = 'access_page'),
    path('signup/',signup_page,name="signup_page"),
    path('chatbot/',chatbot_page,name="chatbot_page"),
    path('control/',control_page, name='control_page'),
    path('dashboard/',dashboard_page, name='dashboard_page'),
    path('calender/',calender_page, name='calender_page'),
    path('email/',email_page, name="email_page"),
    path('chat_reciever/',chatbot_reciever_page, name='chatbot_reciever_page'),
>>>>>>> fc3446c8 (Your commit message)

    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('access/', access_page, name='access_page'),
    path('chatbot/', chatbot_page, name='chatbot_page'),
    path('logout/', logout_user, name='logout_user'),
    path('control/', control_page, name='control_page'),
    path('calender/', calender_page, name='calender_page'),


]
