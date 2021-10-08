# Import Packages
import matplotlib.pyplot as plt
import random

'''
Dice Simulation Function (Testing Law of Large Numbers)
0 --> Head
1 --> Tail
'''


def simulation(num):
    sides = [0]*6
    plt.figure('Dice Experiment')

    for i in range(num):

        # Counting number of times Head and Tail
        sides[random.randint(1, 6) - 1] += 1

        # Every sqrt(num) iteration and last simulation update the chart
        if i % int(num**0.5) == 0 or i == (num-1):
            plt.title('Dice Experiment', fontweight='bold')
            plt.ylabel('Frequency')
            plt.bar(
                ['1', '2', '3', '4', '5', '6'],
                sides,
                color='lightblue'
            )

            for i, val in enumerate(sides):
                plt.text(
                    i, val//2, str(round(100 * val/sum(sides)))+'%', fontweight='bold')
            plt.pause(0.001)
            plt.clf()  # Clear the figure

    plt.show()


# Calling simulation func
num = int(input("How many Dice experiments you want to do? "))
simulation(num)
