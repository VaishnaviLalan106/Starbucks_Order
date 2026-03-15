class Coffee:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Order:
    def __init__(self):
        self.items=[]
    def add_items(self,coffee):
        self.items.append(coffee)
        print(f"{coffee.name} added to order.\n")
    def total(self):
        return sum(coffee.price for coffee in self.items)
        
    def show_order(self):
        if not self.items:
            print("No items in the order.")
            return 
        print("Your Order:")
        for i, item in enumerate(self.items,1):
            print(f"{i}. {item.name} - \u20B9{item.price:.2f}")
        print(f"Total: \u20B9{self.total():.2f}\n")
    def checkout(self):
            if not self.items:
                print("Your cart is empty")
                return
            self.show_order()
            confirm=input("Do you want to proceed to checkout? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Order confirmed! Thank you for your purchase.")
            else:               
                print("Order cancelled.")
def main():
    menu =[
        Coffee("Espresso", 350),
        Coffee("Latte", 450),
        Coffee("Cappuccino", 230),
        Coffee("Americano", 830)
    ]
    order=Order()
    while True:
        print("\n-- Coffee Menu --")
        for i, coffee in enumerate(menu,1):
            print(f"{i}. {coffee.name} - \u20B9{coffee.price:.2f}")
        print("5.View Order")
        print("6.Checkout" )
        print("7.Exit\n")
        choice = input("Please select an option: ")
        if choice in ["1","2","3","4"]: 
            order.add_items(menu[int(choice)-1])      
        elif choice == "5":
            order.show_order()
        elif choice == "6":
            order.checkout()
        elif choice == "7":
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
    