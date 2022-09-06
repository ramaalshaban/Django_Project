from . import views
from django.urls import path
# namespace
app_name = 'kurulus'


urlpatterns = [

    path('', views.ApiOverview, name='home'),

    # path("",views.kurulus_list,name="filter"),
    path('create/', views.add_kurulus, name='add_kurulus'),
    path('update/<int:pk>/', views.update_kurulus, name='update-kurulus'),
    path('all/', views.view_kurulus, name='view_kurulus'),
    path('item/<int:pk>/delete/', views.delete_kurulus, name='delete-kuruls'),

    path("filter/",views.kurulus_filter,name="filter"),



]