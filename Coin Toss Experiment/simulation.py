# Import Packages
import matplotlib.pyplot as plt
import random

'''
Coin Toss Simulation Function (Testing Law of Large Numbers)
0 --> Head
1 --> Tail
'''


def simulation(num):
    sides = [0]*2
    plt.figure('Coin Toss Experiment')

    for i in range(num):

        # Counting number of times Head and Tail
        sides[random.randint(0, 1)] += 1

        # Every sqrt(num) iteration and last simulation update the chart
        if i % int(num**0.5) == 0 or i == (num-1):
            plt.title('Coin Toss Experiment', fontweight='bold')
            plt.ylabel('Frequency')
            plt.bar(
                ['Head', 'Tail'],
                sides,
                color='lightblue'
            )
            plt.text(
                0, sides[0]//2, str(round(100 * sides[0]/sum(sides)))+'%', fontweight='bold')
            plt.text(
                1, sides[1]//2, str(round(100 * sides[1]/sum(sides)))+'%', fontweight='bold')
            plt.pause(0.001)
            plt.clf()  # Clear the figure

    plt.show()


# Calling simulation func
num = int(input("How many Coin Toss you want to do? "))
simulation(num)
