from django.shortcuts import render
from django.core.cache import cache
from .api_handler import api_request
from .translator_handler import translate
# Create your views here.

def avatar_character_list(request):
    avatar_api_data = cache.get('avatar_api_data')
    
    if not avatar_api_data:
        avatar_api_data = api_request('https://last-airbender-api.fly.dev/api/v1/characters', 'GET')
        cache.set('avatar_api_data', avatar_api_data, timeout=60*60)

    for character in avatar_api_data:
        name = character.get('name')
        affiliation = character.get('affiliation', 'Unknown')

        translated_name = translate(name, 'pt')
        translated_affiliation = translate(affiliation, 'pt')

        character['name'] = translated_name
        character['affiliation'] = translated_affiliation

    return render(request, 'character_list.html', {'characters': avatar_api_data})
