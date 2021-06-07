import random
numberOfStreaks = 0
sequenceOfFlips = []
counter = 0
previous_flip = None

for experimentNumber in range(10000):
    #Code that creates a list of 100 'heads' or 'tails' values.

    for flip in range(100):
        if random.randint(0,1) == 0:
            # Zero is heads
            sequenceOfFlips.append('H')
        else:
            sequenceOfFlips.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.

    for flip in sequenceOfFlips:

        if flip == previous_flip:
            counter += 1
            previous_flip = flip
        else:
            counter = 0
            previous_flip = flip
        if counter == 100:
            numberOfStreaks += 1
            break




print('Chance of streak: {}'.format(numberOfStreaks/100))
