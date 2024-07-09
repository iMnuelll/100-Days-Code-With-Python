from data import MENU, resources, profit

def check_resources(order_ingredients) :
    """Return True when the order can be made, False otherwise"""
    for item in order_ingredients :
        if order_ingredients[item] > resources[item] :
            print(f"Sorry, there is not enough {item}")
            return False
        return True

def process_coins() :
    """Return the total calculated coins"""
    print("Please insert Coins")
    total = int(input("How many Quarters? : ")) * 0.25
    total += int(input("How many Dimes? : ")) * 0.1
    total += int(input("How many Nickels? : ")) * 0.05
    total += int(input("How many Pennies? : ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost) :
    """Return True when transaction is successful, False otherwise"""
    if money_received > drink_cost :
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change {change}")
        global profit
        profit += drink_cost
        return True
    else :
        print("Sorry, there is not enough. Money refunded.")
        return False

def make_coffe(drink_name, order_ingredients) :
    """Deduct the required ingredients from resources"""
    for item in order_ingredients :
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕. Enjoy...")

is_on = True

while is_on :
    choice = input("What would you like? (espresso/latte/cappucino) : ").lower()
    if choice == "off" :
        is_on = False
    elif choice == "report" :
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee Beans : {resources['coffee']}g")
        print("Profit : ${profit}")
    else :
        drink = MENU[choice]
        if check_resources(drink["ingredients"]) :
            money_received = process_coins()
            if is_transaction_successful(money_received, drink["cost"]) :
                make_coffe(choice, drink["ingredients"])