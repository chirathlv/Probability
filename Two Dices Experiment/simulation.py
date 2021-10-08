# Import Packages
import matplotlib.pyplot as plt
import random

'''
Two Dices Simulation Function (Testing Law of Large Numbers)
0 --> Head
1 --> Tail
'''


def simulation(num):
    sides = [0]*11
    plt.figure('Two Dices Experiment')

    for i in range(num):

        # Counting number of times Head and Tail
        dice_1_side = random.randint(1, 6)
        dice_2_side = random.randint(1, 6)
        sides[dice_1_side+dice_2_side-2] += 1

        # Every sqrt(num) iteration and last simulation update the chart
        if i % int(num**0.5) == 0 or i == (num-1):
            plt.title('Two Dices Experiment', fontweight='bold')
            plt.ylabel('Frequency')
            plt.bar(
                ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                sides,
                color='lightblue'
            )

            for i, val in enumerate(sides):
                plt.text(
                    i-0.3, val//2, str(round(100 * val/sum(sides)))+'%', fontweight='bold')
            plt.pause(0.001)
            plt.clf()  # Clear the figure

    plt.show()


# Calling simulation func
num = int(input("How many Two Dices experiments you want to do? "))
simulation(num)
