# 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
# nombre
# numero_de_estrellas
# habitaciones
# El value del key de habitaciones debe ser una lista, y cada habitación debe tener 
# la siguiente información:
# numero
# piso
# precio_por_noche

hotel_name = input("Enter the hotel's name: ")
hotel_stars = int(input("Enter the hotel's stars quantity: "))
rooms_qty = int(input("Enter the hotel's quantity of rooms: "))
rooms_list=[]
rooms_counter=1

print("")

while(rooms_counter<=rooms_qty):
    print(f"--- Room # {rooms_counter} ----")
    hotel_room = {
    "room_number":int(input(f"Enter the #{rooms_counter} room's number: ")),
    "room_floor":int(input(f"Enter the #{rooms_counter} room's floor: ")),
    "room_nightly_price":float(input(f"Enter the #{rooms_counter} room's nightly price: "))
    }
    rooms_list.append(hotel_room)
    rooms_counter+=1

hotel_info = {
    "name":hotel_name,
    "stars":hotel_stars,
    "rooms":rooms_list
}

print("")
print(f"The created dictionary for the hotel is: {hotel_info}")

#Testing printing some rooms by dictionary[rooms_key][list_index]
print(f"The first room in the list is: {hotel_info["rooms"][0]}, and fourth room is {hotel_info["rooms"][3]}")