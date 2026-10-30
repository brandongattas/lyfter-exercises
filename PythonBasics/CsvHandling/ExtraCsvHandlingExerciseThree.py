# 3. Cree un programa que abra un archivo .csv con la información de 
# videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
#     Lea el archivo .csv con videojuegos
#     Cuente cuántos videojuegos hay de cada género
#     Muestre el resultado de forma ordenada
#     Ejemplo:
#         Salida:
#             Géneros encontrados:
#             Acción: 5
#             Aventura: 3
#             Deportes: 4
#             ...

import csv
import os

FILE_NAME = 'games_details.csv'

def get_csv_as_list_of_dict(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		reader = csv.DictReader(file)
		return list(reader)

def read_csv_file_and_print(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		reader = csv.DictReader(file)
		for item in reader:
			print(item)

def print_games_by_genre_count(my_games):
	genre='genre'
	genres_count={}
	for item in my_games:
		if item[genre] in genres_count:
			genres_count[item[genre]]+=1
		else:
			genres_count[item[genre]]=1

	for key,value in genres_count.items():
		print(f'{key}: {value}')

def get_absolute_file_path(file_name):
	script_dir = os.path.dirname(os.path.abspath(__file__))
	return os.path.join(script_dir, file_name)

def main():
	try:
		print("---Available Games: ----")
		read_csv_file_and_print(get_absolute_file_path(FILE_NAME))
		games=get_csv_as_list_of_dict(get_absolute_file_path(FILE_NAME))
		
		print("")
		print(f"Found genres: ")
		print_games_by_genre_count(games)

		
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()