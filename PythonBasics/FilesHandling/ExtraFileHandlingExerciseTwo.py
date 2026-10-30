# 2. Cree un programa que abra un archivo de texto y cuente 
# cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o 
# saltos de línea)
# Ejemplo:
#     Salida:
#         "Este archivo contiene " 123 "palabras"

def read_file_return_text(path):
	with open(path, 'r', encoding='utf-8') as file:
		return file.read()

def count_words_in_str(my_string):
	return len(my_string.split())

def get_subfolder_name():
    full_path=__file__
    path_parts = full_path.split('\\')
    return path_parts[-2]

def main():
	try:
		text_from_file = read_file_return_text(f"{get_subfolder_name()}\\count_words.txt")
		print(f"This file contains: {count_words_in_str(text_from_file)} words.")
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()