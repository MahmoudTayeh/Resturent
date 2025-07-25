from django.urls import path
from . import views  

urlpatterns = [
    path('dashboard_owner/', views.dashboaard_owner , name='dashboard_owner'),
    path('login/', views.login , name='login'),
    path('register/', views.register , name='register'),
    path('dashboard_owner/forgotPassword/', views.forgotPassword , name='forgotPassword'),
    path('dashboard_owner/page_404/', views.page_404 , name='page_404'),
    path('dashboard_owner/blank_page/', views.blank_page , name='blank_page'),
    path('dashboard_owner/charts/', views.charts , name='charts'),
    path('dashboard_owner/tables/', views.tables , name='tables'),
]
