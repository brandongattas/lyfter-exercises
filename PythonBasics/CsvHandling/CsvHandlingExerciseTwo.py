# Lea sobre el resto de métodos del módulo csv aqui y cree 
# una version alternativa del ejercicio de arriba que 
# guarde el archivo separado por tabulaciones en vez de 
# por comas.
# Ejemplo de archivo final:
#     nombre	genero	desarrollador	clasificacion
#     Grand Theft Auto IV	Accion	Rockstar Games	M
#     The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
#     Tony Hawk's Pro Skater 2	Deportes	Activision	T

import csv
import os

FILE_NAME='games_details_delimiter.csv'

def save_games_details(file_path, data):
	with open(file_path, 'w', encoding='utf-8', newline='') as file:
		headers = data[0].keys()
		writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
		writer.writeheader()
		writer.writerows(data)

def read_csv_file(file_path):
	with open(file_path, 'r', newline='', encoding='utf-8') as file:
		reader = csv.DictReader(file)
		for row in reader:
			print(row)

def enter_qty_games():
	while True:
		try:
			user_input=input("Enter the quantity of games to be saved: ")
			qty_games = int(user_input)
			return qty_games
		except ValueError:
			print("#### The number is invalid, please enter a valid quantity number - integer. ####\n")

def enter_game_details_get_list_of_dict():
	qty_games=enter_qty_games()
	counter=1
	games_list_of_dict=[]
	while counter<=qty_games:
		name=f"{input(f"Enter #{counter} game's name: ")}"
		genre=f"{input(f"Enter #{counter} game's genre: ")}"
		developer=f"{input(f"Enter #{counter} game's developer name: ")}"
		esrb_rating=f"{input(f"Enter #{counter} game's ESRB rating: ")}"
		game_dict={'name':name, 'genre':genre, 'developer':developer, 'esrb_rating':esrb_rating}
		games_list_of_dict.append(game_dict)
		counter+=1
	return games_list_of_dict

def get_absolute_file_path(file_name):
	script_dir = os.path.dirname(os.path.abspath(__file__))
	return os.path.join(script_dir, file_name)


def main():

	try:
		games_details=enter_game_details_get_list_of_dict()
		print(f"List of Dictionaries created: {games_details}")
		save_games_details(get_absolute_file_path(FILE_NAME), games_details)
		print("")
		print("games_details.csv content: ")
		read_csv_file(get_absolute_file_path(FILE_NAME))
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()