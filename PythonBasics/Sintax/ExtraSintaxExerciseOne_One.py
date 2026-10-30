#  Cree un programa que le pida un precio de producto al usuario, calcule su descuento 
#  y muestre el precio final tomando en cuenta que:
#       1. Si el precio es menor a 100, el descuento es del 2%.
#       2. Si el precio es mayor o igual a 100, el descuento es del 10%.
#  Ejemplos:
#  120 → 108
#  40 → 39.2


product_price = int(input("Provide the product's price: "))
final_product_price = 0

if product_price >= 100:
    final_product_price = product_price*0.9
else:
    final_product_price = product_price*0.98

print(f"Final product price including the discount: {final_product_price}")