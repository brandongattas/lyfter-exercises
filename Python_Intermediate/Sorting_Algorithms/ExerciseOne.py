# 1. Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):
        has_made_changes = False

        for index in range(0, len(list_to_sort)-1-outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index+1]

            print(f"--Iteration {index} | {outer_index}. Current element: {current_element}, Next element: {next_element}")
            
            if current_element > next_element:
                print("Current element is greater than the next one. switching it...")
                list_to_sort[index] = next_element
                list_to_sort[index+1] = current_element
                has_made_changes = True

        if not has_made_changes:
            return

my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
bubble_sort(my_test_list)

print(my_test_list)