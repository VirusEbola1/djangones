
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Task, Game
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

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
    game_url = request.build_absolute_uri(game.rom_file.url)
    rom_file_url = game.rom_file.url
    return render(request, 'tasks/game_detail.html', {'game': game, 'game_url': game_url, 'rom_file_url': rom_file_url})


def dendy_game_rom(request, rom_file):
    # Получить объект игры на основе имени файла ROM
    game = get_object_or_404(Game, rom_file=rom_file)

    with open(game.rom_file.path, 'rb') as rom:
        response = HttpResponse(rom.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(rom_file)
        return response
    
@csrf_exempt
def load_game_rom(request):
    if request.method == 'POST':
        rom_file = request.FILES.get('rom_file')
        if rom_file:
            rom_content = rom_file.read()
            return JsonResponse({'rom_content': rom_content.decode('utf-8')})
        else:
            return JsonResponse({'error': 'No ROM file provided'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to some page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')  # Redirect to some page after login
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})