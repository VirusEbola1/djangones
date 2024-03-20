from django.contrib import admin
from django.urls import path
from tasks.views import task_list, dendy_games, sega_games, game_detail_sega, user_login  # Используем game_detail_sega вместо game_detail
from tasks import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('dendy/', dendy_games, name='dendy_games'),  
    path('sega/', sega_games, name='sega_games'), 
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),  # Этот URL-шаблон оставляем для game_detail
    path('dendy/<path:rom_file>/', views.dendy_game_rom, name='dendy_game_rom'),
    path('register/', views.register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='task_list'), name='logout'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('game_sega/<int:game_id>/', game_detail_sega, name='game_detail_sega'),  # Используем game_detail_sega
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
