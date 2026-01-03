cart = []

def add_product():
    product = input("Enter product name: ")
    price = input("Enter product price: ")
    cart.append({"product": product, "price": price})
    print("Product added to cart")

def view_cart():
    if not cart:
        print("Cart is empty")
    else:
        for item in cart:
            print(item["product"], "-", item["price"])

def main():
    while True:
        print("1. Add Product")
        print("2. View Cart")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
