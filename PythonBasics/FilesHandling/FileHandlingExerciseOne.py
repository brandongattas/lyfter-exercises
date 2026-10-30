# Cree un programa que lea nombres de canciones de un archivo 
# (línea por línea) y guarde en otro archivo los mismos nombres 
# ordenados alfabéticamente.


def read_file_by_lines_return_list(path):
	with open(path, 'r', encoding='utf-8') as file:
		list_of_songs = file.readlines()

		list_without_line_separator=[]
		for song in list_of_songs:
			print(song.strip())
			list_without_line_separator.append(song.strip())

	return list_without_line_separator

def write_new_file_from_list(path, my_list):
	with open(path, 'w', encoding='utf-8') as file:
		for line in my_list:
			file.write(line+'\n')

def get_subfolder_name():
    full_path=__file__
    path_parts = full_path.split('\\')
    return path_parts[-2]

def main():

	try:
		#Read songs from file
		list_of_songs=read_file_by_lines_return_list(f'{get_subfolder_name()}\\song_names.txt')
		
		list_of_songs.sort() #Sorted alphabetically

		#Write new file with sorted list of songs
		write_new_file_from_list(f'{get_subfolder_name()}\\sorted_songs.txt', list_of_songs)

		print("")
		print("sorted_songs.txt file:")
		#Read new created file with sorted song names
		read_file_by_lines_return_list(f'{get_subfolder_name()}\\sorted_songs.txt')


	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()

