# 3. Cree un programa que abra un archivo .json con la información de Pokémon 
# ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
# Ejemplo:
#     Salida:
#         Nombre: Pikachu
#         Ataque: 55
#         Defensa: 40
#         Velocidad: 90

#         Nombre: Bulbasaur
#         Ataque: 49
#         Defensa: 49
#         Velocidad: 45

import json
from pathlib import Path


def get_absolute_file_path(file_name):
    script_dir = Path(__file__).resolve().parent
    return script_dir / file_name

def parse_json_file(file_path):
    # .read_text() opens, reads, and closes the file automatically
    raw_data=file_path.read_text(encoding='utf-8')
    return json.loads(raw_data)

def print_pokemon_main_details(pokemon_inventory):
	counter=1
	for pokemon in pokemon_inventory:
		print(f"---- Pokemon #{counter}: ----")
		print(f'Name: {pokemon["name"]}')
		print(f'Type: {pokemon["type"]}')
		print(f'Attack: {pokemon["stats"]["attack"]}')
		print(f'Defense: {pokemon["stats"]["defense"]}')
		print(f'Speed: {pokemon["stats"]["speed"]}')
		counter+=1

def main():
	FILE_NAME='pokemons.json'
	try:
		pokemons_inventory = parse_json_file(get_absolute_file_path(FILE_NAME))
		print_pokemon_main_details(pokemons_inventory)
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()