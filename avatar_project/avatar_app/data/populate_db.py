'''from handlers.api_handler import api_request
from handlers.translator_handler import translate
from avatar_app.models import AvatarCharacter


def populate_avatar_character():
    avatar_api_data = api_request('https://last-airbender-api.fly.dev/api/v1/characters', 'GET')

    for character in avatar_api_data:
        name = character.get('name')
        affiliation = character.get('affiliation', 'Unknown')

        translated_name = translate(name, 'pt')
        translated_affiliation = translate(affiliation, 'pt')

        character['name'] = translated_name
        character['affiliation'] = translated_affiliation
    
    for character_data in avatar_api_data:
        name = character_data.get('name', 'Unknown')
        affiliation = character_data.get('affiliation', 'Unknown')
        allies = character_data.get('allies', 'Unknown')
        enemies = character_data.get('enemies', 'Unknown')
        photoUrl = character_data.get('photoUrl', 'Unknown')

        character = AvatarCharacter(name = name, affiliation = affiliation, allies = allies, enemies = enemies, photoUrl = photoUrl)
        character.save()

        print("Adicionado com sucesso!")'''