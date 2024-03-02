from django.contrib import admin
from django.urls import path
from tasks.views import task_list ,  dendy_games, sega_games , game_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('dendy/', dendy_games, name='dendy_games'),  
    path('sega/', sega_games, name='sega_games'), 
    path('game/<int:game_id>/', game_detail, name='game_detail'),
]
