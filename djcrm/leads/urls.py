from django.urls import path, include
from .views import lead_list, lead_detail, lead_create, lead_update

app_name = "leads"

urlpatterns = [
    path('', lead_list ),
    path('create/', lead_create),
    path('<int:pk>/', lead_detail),
    path('<int:pk>/update/', lead_update),

    
]