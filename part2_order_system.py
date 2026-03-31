# ----- GIVEN DATA (must be included) -----

menu = {
 "Paneer Tikka": {"category": "Starters", "price": 180.0, "available": True},
 "Chicken Wings": {"category": "Starters", "price": 220.0, "available": False},
 "Veg Soup": {"category": "Starters", "price": 120.0, "available": True},
 "Butter Chicken": {"category": "Mains", "price": 320.0, "available": True},
 "Dal Tadka": {"category": "Mains", "price": 180.0, "available": True},
 "Veg Biryani": {"category": "Mains", "price": 250.0, "available": True},
 "Garlic Naan": {"category": "Mains", "price": 40.0, "available": True},
 "Gulab Jamun": {"category": "Desserts", "price": 90.0, "available": True},
 "Rasgulla": {"category": "Desserts", "price": 80.0, "available": True},
 "Ice Cream": {"category": "Desserts", "price": 110.0, "available": False},
}
# TASK 1: Print the menu in a user-friendly format, grouped by category. For each item, show the name, price, and availability status.  
# grouping menu
cats = []

for item in menu:
    cat = menu[item]["category"]
    if cat not in cats:
        cats.append(cat)

for c in cats:
    print("=====", c, "=====")
    
    for item in menu:
        if menu[item]["category"] == c:
            price = menu[item]["price"]
            status = "Available" if menu[item]["available"] else "Unavailable"
            print(item, "₹"+str(price), "["+status+"]")

# CART (simple version)
# we will create a simple cart system where we can add items by name and quantity. The cart will be a list of dictionaries, each representing an item in the cart with its name, quantity, and price.
cart = []

def add_item(name, qty):
    
    if name not in menu:
        print("Item not found")
        return
    
    if not menu[name]["available"]:
        print("Item not available")
        return
    
    found = False
    
    for c in cart:
        if c["item"] == name:
            c["quantity"] += qty
            found = True
    
    if not found:
        cart.append({
            "item": name,
            "quantity": qty,
            "price": menu[name]["price"]
        })

# ORDER SUMMARY
# we will calculate the subtotal, GST, and total for the items in the cart. We will also print a summary of the order with item names, quantities, and total price for each item.
subtotal = 0

for c in cart:
    item_total = c["quantity"] * c["price"]
    subtotal += item_total
    print(c["item"], "x"+str(c["quantity"]), "₹"+str(item_total))

gst = subtotal * 0.05
total = subtotal + gst

print("Subtotal:", subtotal)
print("GST:", round(gst,2))
print("Total:", round(total,2))