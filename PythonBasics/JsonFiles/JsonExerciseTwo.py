# 1. Cree un programa que permita agregar un Pokémon nuevo al 
# archivo de la lección de Manejo de JSON.
#     Debe leer el archivo para importar los Pokémones existentes.
#     Luego debe pedir la información del Pokémon a agregar.
#     Finalmente debe guardar el nuevo Pokémon en el archivo.

import json
from pathlib import Path


def get_absolute_file_path(file_name):
    script_dir = Path(__file__).resolve().parent
    return script_dir / file_name

def parse_json_file(file_path):
    # .read_text() opens, reads, and closes the file automatically
    raw_data = file_path.read_text(encoding='utf-8')
    return json.loads(raw_data)

def save_json_file(file_path, data):
    # 1. Convert the data dictionary to a formatted string
    json_string = json.dumps(data, indent=3)
    
    # 2. Write that string directly to the file (automatically opens and closes it)
    file_path.write_text(json_string, encoding='utf-8')


def ask_for_int(prompt_message):
	while True:
		try:
			return int(input(prompt_message))
		except ValueError:
			print("Invalid input. Please enter a whole number.")

def ask_for_float(prompt_message):
	while True:
		try:
			return float(input(prompt_message))
		except ValueError:
			print("Invalid input. Please enter number using decimals Ex. 6.0")

def ask_for_true_or_false(prompt_message):
	while True:
		user_input=input(prompt_message)
		user_input = user_input.lower()
		if user_input in ('y','yes'):
			return True
		elif user_input in ('n','no'):
			return False

def ask_and_create_list_of_strings(prompt_message):
	user_inputs_list=[]
	input_counter=1
	keep_asking=True
	while keep_asking:
		user_input=input(f'{prompt_message} #{input_counter} (or type "done" to stop): ')
		if user_input.lower()=='done':
			keep_asking=False
		else:
			user_inputs_list.append(user_input)
			input_counter+=1
	return user_inputs_list

def collect_new_pokenmon_details():
	print("---- Enter New Pokemon Details ----")
	poke_name=input("Enter name: ")
	poke_type=input("Enter type: ")
	poke_level=ask_for_int("Enter level: ")
	poke_weight_kg=ask_for_float("Enter weight in Kg as decimal number: ")
	poke_is_shiny=ask_for_true_or_false("Enter if pokemon is shiny (yes/no): ")
	poke_held_item=input("Enter item held by pokemon: ")
	poke_skill_list=ask_and_create_list_of_strings("Enter skill")
	poke_stats_dict={
					"hp":ask_for_int("Enter hp: "),
			"attack":ask_for_int("Enter attack: "),
			"defense":ask_for_int("Enter defense: "),
			"sp_attack":ask_for_int("Enter special attack: "),
			"sp_defense":ask_for_int("Enter special defense: "),
			"speed":ask_for_int("Enter speed: ")
	}

	new_pokemon={
		"name":poke_name,
		"type":poke_type,
		"level":poke_level,
		"weight_kg":poke_weight_kg,
		"is_shiny":poke_is_shiny,
		"held_item":poke_held_item if poke_held_item != "" else None,
		"skills":
			poke_skill_list,
		"stats":
			poke_stats_dict
	}
	return new_pokemon


def main():
	FILE_NAME='pokemons.json'
	try:
		pokemons_inventory = parse_json_file(get_absolute_file_path(FILE_NAME))
		new_pokemon_details=collect_new_pokenmon_details()
		pokemons_inventory.append(new_pokemon_details)
		save_json_file(get_absolute_file_path(FILE_NAME), pokemons_inventory)
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()