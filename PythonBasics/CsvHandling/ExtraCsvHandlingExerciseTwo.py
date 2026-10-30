# 2. Cree un programa que abra un archivo .csv con la información 
# de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
#     Lea el archivo CSV de videojuegos
#     Pida al usuario una clasificación ESRB (por ejemplo: "T")
#     Muestre todos los videojuegos que tengan esa clasificación

import csv
from pathlib import Path

FILE_NAME = 'games_details.csv'

def get_csv_as_list_of_dict(file_path):
	with file_path.open('r', encoding='utf-8') as file:
		reader = csv.DictReader(file)
		return list(reader)

def read_csv_file_and_print(file_path):
	with file_path.open('r', encoding='utf-8') as file:
		reader = csv.DictReader(file)
		for item in reader:
			print(item)

def print_filtered_games(my_games, filter_value):
	counter=0
	for item in my_games:
		if item['esrb_rating'].lower()==filter_value.lower():
			print(item)
			counter+=1
	print(f"There are a total of {counter} games with Rating {filter_value}")

def get_absolute_file_path(file_name):
	script_dir = Path(__file__).resolve().parent
	return script_dir / file_name

def main():
	try:
		print("---Available Games: ----")
		read_csv_file_and_print(get_absolute_file_path(FILE_NAME))
		games=get_csv_as_list_of_dict(get_absolute_file_path(FILE_NAME))
		print("")
		esrb_rating=input("Enter the required ESRB Rating to apply the filter: ")
		print("")
		print(f"Filtered games by ESRB rating: {esrb_rating}")
		print_filtered_games(games,esrb_rating)


		
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()
