# Basic Function
def my_function() :
    print("Hello, world!")
    print("Good Bye, world!")
my_function()

'''For Loop
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
NOTE : TRY THIS CODE JUST ON THE LINK
Hurdle 1
def turn_right() :
    turn_left()
    turn_left()
    turn_left()
def jump() :
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range (6) :
    jump()

# While Loop
Hurdle 2
def turn_right() :
    turn_left()
    turn_left()
    turn_left()
def jump() :
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True :
    jump()

Hurdle 3
def turn_right() :
    turn_left()
    turn_left()
    turn_left()
def jump() :
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True :
    if front_is_clear() :
        move()
    elif wall_in_front () :
        jump()

Hurdle 4
'''