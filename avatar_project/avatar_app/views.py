from django.shortcuts import render
from .models import AvatarCharacter
# Create your views here.

def avatar_character_list(request):
    characters = AvatarCharacter.objects.all()
    return render(request, 'template/lista_character.html', {'characters': characters})
