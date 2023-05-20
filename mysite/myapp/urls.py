from django.urls import path

from . import views
from myapp.views import (
    home_screen_view

)

urlpatterns = [

    path(' ',home_screen_view),
    

]