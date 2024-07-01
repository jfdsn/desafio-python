from django.shortcuts import render
from .api_handler import api_request
from .translator_handler import translate
# Create your views here.

def avatar_character_list(request):
    avatar_api_data = api_request('https://last-airbender-api.fly.dev/api/v1/characters', 'GET')

    for character in avatar_api_data:
        name = character.get('name')
        affiliation = character.get('affiliation', 'Unknown')

        translated_name = translate(name, 'pt')
        translated_affiliation = translate(affiliation, 'pt')

        character['name'] = translated_name
        character['affiliation'] = translated_affiliation

    return render(request, 'character_list.html', {'characters': avatar_api_data})
