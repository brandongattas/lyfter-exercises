# 2. Modifica el bubble_sort para que funcione de derecha a izquierda, 
# ordenando los números menores primero (como en la imagen de abajo).
#
# Este hace lo mismo que el resto, solo que recorre la lista de derecha a izquierda, 
# y las “burbujas” son los elementos menores, no los mayores.

def bubble_sort_inverted(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):
        has_made_changes = False

        for index in range(len(list_to_sort)-1, 0+outer_index, -1):
            current_element = list_to_sort[index]
            prev_element = list_to_sort[index-1]

            print(f"--Iteration {index} | {outer_index}. Current element: {current_element}, Next element: {prev_element}")
            
            if current_element < prev_element:
                print("Current element is greater than the previous one. switching it...")
                list_to_sort[index] = prev_element
                list_to_sort[index-1] = current_element
                has_made_changes = True

        if not has_made_changes:
            return

my_test_list = [1, 2, 45, 20, 4, 3, -1, 0]
bubble_sort_inverted(my_test_list)

print(my_test_list)