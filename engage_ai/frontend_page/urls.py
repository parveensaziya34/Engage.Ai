from django.urls import path
from frontend_page.views import login_page,access_page,signup_page,chatbot_page
urlpatterns = [
    path('login/', login_page,name = "signin_page"),
    path('access/',access_page),
    path('signup/',signup_page,name="signup_page"),
    path('chatbot/',chatbot_page),


]
