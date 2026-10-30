# 1. Cree un programa que lea un archivo con texto línea por línea,
# quite los saltos de línea (\n) y escriba todo el contenido en 
# un solo renglón en un nuevo archivo
# Ejemplo:
# Entrada:
#     Hola
#     mundo
#     esto
#     es
#     Python

# Salida:
#     "Hola mundo esto es Python"



def read_file_return_list(path):
	with open(path, 'r', encoding='utf-8') as file:
		return [line.rstrip('\n') for line in file.readlines()]

def write_file_from_list(path, my_list):
	with open(path, 'w', encoding='utf-8') as file:
		for record in my_list:
			file.write(record+" ")

def read_file(path):
	with open(path, 'r', encoding='utf-8') as file:
		content = file.read()
		print(content)

def get_subfolder_name():
    full_path=__file__
    path_parts = full_path.split('\\')
    return path_parts[-2]

def main():
	try:
		print("hola_mundo.txt:")
		read_file(f"{get_subfolder_name()}\\hola_mundo.txt")

		my_list = read_file_return_list(f"{get_subfolder_name()}\\hola_mundo.txt")
		write_file_from_list(f"{get_subfolder_name()}\\single_line_file.txt", my_list)
		
		print("")
		print("single_line_file.txt:")
		read_file(f"{get_subfolder_name()}\\single_line_file.txt")
	except Exception as ex:
		print(ex)


if __name__ == '__main__':
	main()