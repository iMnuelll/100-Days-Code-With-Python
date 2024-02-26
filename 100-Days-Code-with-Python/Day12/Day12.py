'''This is Global Scope'''
enemies = 1

def increase_enemies():
  '''This is Local Scope'''
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

'''Change the global scope variable with local variable scope'''
enemies = 1
def increase_enemies():
  return enemies + 1

enemies = increase_enemies()
print(f"After change the global scope variable: {enemies}")

'''Global Constants : Is a variable that has a fixed value and cannot be changed during program execution'''
PI = 3.14
URL = "https://github.com/"