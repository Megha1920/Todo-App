from django.urls import path
from tasks.views import home , logins , signup , add_todo , signout , delete_todo,update_todo


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,logins  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('update-todo/<int:id>' , update_todo ,name=' update_todo'), 
   path('logout/' , signout ), 
]