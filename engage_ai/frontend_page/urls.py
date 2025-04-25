from django.urls import path
from frontend_page.views import login_page,access_page
urlpatterns = [
    path('login/', login_page),
    path('access/',access_page),

]
