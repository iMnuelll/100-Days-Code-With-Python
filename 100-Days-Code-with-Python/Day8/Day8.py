# Function
def greet() :
    print("Hello World")
    print("How are you?")
    print("Isn't the weather good?")
# Call the function
greet()

# Function with arguments

def greet_name (name) :
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"Isn't the weather good {name}?")
# Call the function
greet_name("Angela")

# Function with more than one arguments
def greet_with(name , location) :
    print(f"Hello {name}")
    print(f"Your location at {location}")
greet_with(location = "Makassar", name = "Angela")

# Prime Checker
def prime_checker(number) :
    is_prime = True
    for i in range(2, number) :
        if number % i == 0 :
            is_prime = False
    if is_prime :
        print(f"{number} is a prime number")
    else :
        print(f"{number} is not a prime number")
n = int(input("Input your number from 1 - 100 : "))
prime_checker(number = n)

# New Email
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

result = replace_domain("imanuel@gmail.com", "gmail", "yahoo.com")
print(result)