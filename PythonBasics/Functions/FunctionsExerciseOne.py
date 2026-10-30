# Cree dos funciones que impriman dos cosas distintas, 
# y haga que la primera llame la segunda.

def print_hello_and_call_world_function():
    print("Hello")
    print_world()

def print_world():
    print("world")

print_hello_and_call_world_function()