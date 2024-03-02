from django.shortcuts import render , get_object_or_404
from .models import Task
from .models import Game

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def dendy_games(request):
    dendy_games = Game.objects.filter(platform='Dendy')  # Получаем список игр для Dendy
    return render(request, 'tasks/dendy_games.html', {'dendy_games': dendy_games})

def sega_games(request):
    return render(request, 'tasks/sega_games.html')

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'tasks/game_detail.html', {'game': game})