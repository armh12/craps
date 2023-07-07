import random

def game():
    def random_nums():
        players_roll = random.randint(1,6)
        casinos_roll = random.randint(1,6)
        sum_of_both = players_roll + casinos_roll
        return sum_of_both
    p_win_combinations = [7,11]
    c_win_combinations = [2,3,12]
    sum_of_both = random_nums()
    if sum_of_both in p_win_combinations:
        print(f'The sum of dice is {sum_of_both}')
        print('Player wins!')
    elif sum_of_both in c_win_combinations:
        print(f'The sum of dice is {sum_of_both}')
        print('Casino wins!')
    else:
        print(f'Your goal number is {sum_of_both}!')
        while True:
            goal_sum = random_nums()
            if goal_sum == sum_of_both:
                print(f'The sum of dice is {goal_sum}')
                print('Player wins!')
                break
            elif goal_sum == 7:
                print(f'The sum of dice is {goal_sum}')
                print('Casino wins!')
                break
            else:
                print(f'The sum of dice is {goal_sum}')
                continue 

game()
