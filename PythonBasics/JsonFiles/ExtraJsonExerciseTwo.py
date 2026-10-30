# 2. Cree un programa que abra un archivo .json con la información de Pokémon 
# ( en base al JSON que fue generado en el ejercicio 1) y::
# Lea el archivo JSON de Pokémon
# Pida al usuario un tipo de Pokémon
# Muestre todos los Pokémon que sean de ese tipo
#     Ejemplo:
#         Entrada:
#             "Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): " 
#             "Fuego"

#         Salida:
#             "Los pokemos que existen de ese tipo son: "
#             Charmander
#             Growlithe
#             Victini

import json
from pathlib import Path


def get_absolute_file_path(file_name):
	script_dir = Path(__file__).resolve().parent
	return script_dir / file_name

def parse_json_file(file_path):
	# .read_text() opens, reads, and closes the file automatically
	raw_data = file_path.read_text(encoding='utf-8')
	return json.loads(raw_data)

def print_pokemon_for_a_type(pokemon_inventory):
	poke_type=input("Enter the Pokemon type that you wish to search (water, fire, electric, etc): ").lower()
	counter=0
	print(f"Pokemons that exist under {poke_type} type are:")
	for pokemon in pokemon_inventory:
		if pokemon["type"].lower()==poke_type:
			print(pokemon["name"])
			counter+=1
	print(f"There are {counter} {poke_type} pokemon.")

def main():
	FILE_NAME='pokemons.json'
	try:
		pokemons_inventory = parse_json_file(get_absolute_file_path(FILE_NAME))
		print_pokemon_for_a_type(pokemons_inventory)
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()