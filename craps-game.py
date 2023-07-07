import random

def menu():
    print('''Hello, welcome to Craps game!''')
    _ = input('Type yes if you want to play,any key to exit: ')
    if _ == 'yes':
        game()
    else:
        print('Thank you!')
        
def roll_dice():
    step = input('Press ENTER to roll the dice')
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    return num1 + num2

def game():
    sum_of_dices = roll_dice()
    if sum_of_dices in (7,11):
        print(f'Number is {sum_of_dices}')
        print('Player win!')
    elif sum_of_dices in (2,3,12):
        print(f'Number is {sum_of_dices}')
        print('Casino win!')
    else:
        print(f'There is goal number {sum_of_dices}')
        while True:
            goal_sum = roll_dice()
            if goal_sum == 7:
                print(f'Goal number is {goal_sum}')
                print('Casino win!')
                break
            elif goal_sum == sum_of_dices:
                print(f'Number is {goal_sum}')
                print('Player win!')
            else:
                print(f'Number is {goal_sum}')
                continue
            
menu()
        
