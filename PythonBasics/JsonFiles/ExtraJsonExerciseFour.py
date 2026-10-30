# 4. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON
# Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:
#     Ejemplo:
#         Salida:
#             Tipo: Agua → Promedio de nivel: 42.6
#             Tipo: Fuego → Promedio de nivel: 37.2
#             Tipo: Planta → Promedio de nivel: 30.4

import json
from pathlib import Path

def get_absolute_file_path(file_name):
	script_dir = Path(__file__).resolve().parent
	return script_dir / file_name

def parse_json_file(file_path):
	# .read_text() opens, reads, and closes the file automatically
	raw_data=file_path.read_text(encoding='utf-8')
	return json.loads(raw_data)

def get_pokemon_groupped_by_type_and_level(pokemon_inventory):
	pokemons_grouped={}
	for pokemon in pokemon_inventory:
		if pokemon['type'] in pokemons_grouped:
			pokemons_grouped[pokemon['type']].append(pokemon['level'])
		else:
			pokemons_grouped[pokemon['type']]=[pokemon['level']]
	return pokemons_grouped

def get_avg_from_list(values_list):
	if not values_list:
		return 0 # return 0 in case of values_list empty and avoid ZeroDivision ecxeption
	return sum(values_list) / len(values_list)

def print_level_avg_by_type(pokemon_groups):
	for poke_type in pokemon_groups:
		print(f"Type: {poke_type} -> Average level: {get_avg_from_list(pokemon_groups[poke_type])}")

def main():
	FILE_NAME='pokemons.json'
	try:
		pokemons_inventory = parse_json_file(get_absolute_file_path(FILE_NAME))
		pokemons_grouped_dict=get_pokemon_groupped_by_type_and_level(pokemons_inventory)
		print_level_avg_by_type(pokemons_grouped_dict)
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()