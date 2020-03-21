# Taylor Byers
# Intergration Project - Revised Edition

# Basic Greeting for Program
print("Hello, and welcome to Taylor's intergration project")
name = input("What is your name? ")
print("\nHello", name + "!", "This project is currently a work in progress.")

# Defining Main
def main_menu():
    print("\nPlease Select an option.")
    print("a.) Menu")
    print("b.) Bar")
    print("c.) Employee")
    print("d.) Director")
    option = input("Type the letter of your selection choice or type exit to exit: ")
    if option == ("a"):
        choice_a()
    elif option == ("b"):
        choice_b()     
    elif option == ("c"):
        choice_c()
    elif option == ("d"):
        choice_d()
    elif option == ("exit"):
        print("\nThank you for checking out my intergration project", name + "! I hope you enjoyed it!")
    else: # Invalid choice of a, b, c, or d from main menu
        while option != "a" or option != "b" or option != "c" or option != "d":
            option = input("Sorry you didn't pick an available option, please type a, b, c, or d. ")
            if option == ("a"):
                choice_a()
                break
            elif option == ("b"):
                choice_b()
                break
            elif option == ("c"):
                choice_c()
                break
            elif option == ("d"):
                choice_d()
                break

#Defining Choices
def choice_a():
        print("\nTodays Menu options include: \n ")
        print("Appetizers: " + soup_otd, salad_otd, "House Salad and Coleslaw.", sep=", ")
        print("Entrees: " + entree_otd1, entree_otd2, entree_otd3, "your choice of sandwich, or any of our forever menu items.", sep=", ")
        print("Sides: " + side_otd1, side_otd2, "French fries, Onion Rings, Cottage Cheese, Beets, Applesauce, Green Beans, Carrots, Baked Sweet Potato, and Mashed Potatoes.", sep=", ")
        print("Desserts: " + dessert_otd, icecream_otd, "Bannana split, Strawberry Shortcake, or any of our other flavors of ice cream. \n", sep=", ")
        option_a = input("Care to see our forever menu items? Enter yes or no. ")
        if option_a == "yes": # Picked see extra menu items
            extended_menu()
            main_menu()
        elif option_a == "no": # Picked no to menu items
            menu_goodbye()
            main_menu()
        else: # FINALLY LOOPING PROPERLY
            while option_a != "yes" or option_a != "no":
                option_a = input("Sorry that wasn't a choice, please enter yes or no")
                if option_a == ("yes"):
                    extended_menu()
                    main_menu()
                    break
                elif option_a == ("no"):
                    menu_goodbye()
                    main_menu()
                    break
def choice_b():
    bar_option = input("\nWelcome to the Bar, are you interested in a beer, wine, or cocktail? ")
    if bar_option == ("beer"):
        beer_prompt()
        main_menu()
    elif bar_option == ("wine"):
        wine_prompt()
        main_menu()
    elif bar_option == ("cocktail"):
        cocktail_prompt()
        main_menu()
    else: 
        while bar_option != ("wine") or bar_option != ("beer") or bar_option != ("cocktail"):
            bar_option = input("Sorry the option you picked wasn't available, please type either beer, wine, or cocktail")
            if bar_option == ("beer"):
                beer_prompt()
                main_menu()
                break
            elif bar_option == ("wine"):
                wine_prompt()
                main_menu()
                break
            elif bar_option == ("cocktail"):
                cocktail_prompt()
                main_menu()
                break
def choice_c():
    employee_num_list = open("employee_nums.txt")
    employee_num_check = employee_num_list.read()
    employee_num = input("Please input your employee number: ")
    if employee_num in employee_num_check:
        print("Welcome 'placeholder name'") #Adding names, messing with formatting in text file to do this
    else:
        print("Invalid number input, returning to main menu.")
    main_menu()
def choice_d():
    print("In progress") # Manage otd items
    main_menu()
    
# Required variables for later use - otd = Of the Day
soup_otd = ("soup")
salad_otd = ("salad")
entree_otd1 = ("Entree1")
entree_otd2 = ("Entree2")
entree_otd3 = ("Entree3")
dessert_otd = ("Dessert")
side_otd1 = ("Side1")
side_otd2 = ("Side2")
icecream_otd = ("Ice cream")

#Defining Menu Option Variables:  #May change to be a text file in the future for a ordering system
def extended_menu():
    print("\nAlways available entrees include: Salmon (Poached/Grilled), Caeser Salad, Cobb Salad, Trio Salad")
    print("Penne Pasta (Marinara/Alfredo), Roasted Chicken (Light/Dark), and a Hamburger.")
    print("Flavors of Ice Cream: Vanilla, Chocolate, Strawberry, Sherbert, Spamoni, Kalua, and Cherry Vanilla.")
def menu_goodbye():
    print("\nThank you for viewing todays menu", name + ". We hope you enjoy it!")
#Defining Bar Option Variables:
def beer_prompt():
    print("\nFor beers we have Michelob Ultra, Budweiser, and Budlight.")
def wine_prompt():
    print("\nRed wines: Cabernet, Merlot, and Pinot Noir")
    print("\nWhite Wine: Chardonnay, Pinot Grigio, and White Zinfandel")
def cocktail_prompt():
    print("\nAvailable cocktails: Martini, Margarita, Mannhatten, Old Fashion, and Cosmopolitan")

##### Call to main #####
main_menu()
