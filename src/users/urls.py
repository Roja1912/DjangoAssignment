from django.urls import path
from users.views import GetUsers

urlpatterns = [
    path('getusers/', GetUsers.as_view(
    ), name="getusers"),
]


