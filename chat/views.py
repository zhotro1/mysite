from django.shortcuts import render

def game(request):
	return render(request, 'chat/game.html')

# Create your views here.

def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })