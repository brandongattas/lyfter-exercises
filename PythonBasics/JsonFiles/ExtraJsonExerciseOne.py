# 1. Cree un programa que abra un archivo .json con la información de Pokémon 
# ( en base al JSON que fue generado en el ejercicio 1) y:
#     -Lea el archivo JSON de Pokémon
#     -Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel 
#      (o cualquier otro atributo definido)

import json
from pathlib import Path


def get_absolute_file_path(file_name):
    script_dir = Path(__file__).resolve().parent
    return script_dir / file_name

def parse_json_file(file_path):
    # .read_text() opens, reads, and closes the file automatically
    raw_data = file_path.read_text(encoding='utf-8')
    return json.loads(raw_data)

def print_pokemon_list(pokemon_list):
	for pokemon in pokemon_list:
		poke_name=pokemon["name"]
		poke_type=pokemon["type"]
		poke_level=pokemon["level"]
		print(f'Name: {poke_name} | Type: {poke_type} | Level: {poke_level}')

def main():
	FILE_NAME='pokemons.json'
	try:
		pokemons_inventory = parse_json_file(get_absolute_file_path(FILE_NAME))
		print('#### Pokemon Inventory ####')
		print_pokemon_list(pokemons_inventory)
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()