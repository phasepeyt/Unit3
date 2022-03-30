#oregon trail

import random

#intro
print("welcome to the oregon trail! \n"
"the goal is to travel from independance missouri to oregon by december 1st \n"
"today is march 1st \n")

#global variables
months = ['january','dummy','february','march','april','may','june','july','august','september','october','november','december']
miles_left = 2000
current_day = 1
current_month = 3
month30 = ['april', 'june','september','november']
food = 500
health = 5

#function defs
def travel():
    global miles_left, current_day

    days_this_travel = random.randint(3, 7)
    miles_traveled = random.randint(30, 60)

    print(f"you traveled {miles_traveled} miles")

    miles_left -= miles_traveled
    
    add_day(days_this_travel)

    

def consume(days):
    global food

    food_consumed_this_turn = 5 * days

    food -= food_consumed_this_turn


def badhealth():
    pass



def add_day(days):
    global current_day, current_month, health
    current_day += days

    consume(days)

    




    #month rollover?
    if months[current_month] in month30:
        if current_day > 30:
            current_day -= 30
            current_month += 1 
            health -= 2
    else:
        if current_day > 31:
            current_day -= 31
            current_month += 1
            health -= 2

def rest():
    global health 
    days_this_rest = random.randint(2, 5)
    print(f"you rested for {days_this_rest} days.")

    if health == 5:
        print("why r u wasting time resting at full health?")
    else:
        health += 1
        print("you gained one health")


    add_day(days_this_rest)


    

def status():
    print(f"you have {miles_left} miles to go")
    print(f"it is {months[current_month]} {current_day}")
    print(f"you have {food} lbs of food left")
    print(f"you have {health} health")

def hunt():
    global food

    days_this_hunt = random.randint(2, 5)
    food += 100

    add_day(days_this_hunt)
    print("you gained 100 lbs of food")

def quit():
    global game_over
    print("goodbye!")
    game_over = True

#game loop
game_over = False

while not game_over:
    
    user_choice = input("what would you like to do? ")

    if user_choice == 'travel':
        travel()
    elif user_choice == 'status':
        status()
    elif user_choice == 'hunt':
        hunt()
    elif user_choice == 'rest':
        rest()
    elif user_choice == 'quit':
        quit()
    
    if health == -1:
        game_over == True
        print("you have died")
        quit()

    if current_day == 31 and current_month == 12:
        print("game over")
        game_over == True
        quit()
        
    if miles_left < 0:
        print("you made it!")
        game_over == True
        quit()

    if food < 0:
        print("you have died")
        game_over == True
        quit()

    
