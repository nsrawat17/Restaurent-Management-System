def show_menu():
    print("Welcome to our Resturant")
    print("1. Burger  Rupees - 120")
    print("2. Pizza  Rupees - 180")
    print("3. Pasta  Rupees - 120")
    print("4. Coffee - Rupees - 110")
    print("5. Exit")
def take_order(choice):
    if choice==1:
        print("you ordered burger")
    elif choice==2:
        print("you ordered pizza")
    elif choice==3:
        print("you ordered pasta")
    elif choice==4:
        print("you ordered coffee")
    else:
        print("invalid choice please try again")
show_menu()
user_choice=int(input("enter your choice:"))
take_order(user_choice)            