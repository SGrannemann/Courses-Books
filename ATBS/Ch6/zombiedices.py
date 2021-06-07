import zombiedice
import random


##############################################################################
################ not working as intended #####################################
##############################################################################
#class MyZombie:
    #def __init__(self, name):
        # All zombies must have a name:
    #    self.name = name

    #def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

    #    diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
    #    brains = 0
    #    options = ['continue', 'stop']
    #    while diceRollResults is not None:
            #three shotguns rolled leads to zombiedice.rolls
            #returning None
    #        brains += diceRollResults['brains']

    #        if random.choice(options) == 'continue':
    #            diceRollResults = zombiedice.roll()
    #        else:
    #            break

            #if brains < 2:
            #    diceRollResults = zombiedice.roll() # roll again
            #else:
            #    break

class My_randomChoiceZombie:
    def __init__(self, name):

        self.name = name

    def turn(self, gameState):


        diceRollResults = zombiedice.roll()

        brains = 0
        options = ['continue', 'stop']
        while diceRollResults is not None:
            #three shotguns rolled leads to zombiedice.rolls
            #returning None
            brains += diceRollResults['brains']

            if random.choice(options) == 'continue':
                diceRollResults = zombiedice.roll()
            else:
                break

class My_StopAfterTwoBrains:
    def __init__(self, name):

        self.name = name

    def turn(self, gameState):


        diceRollResults = zombiedice.roll()

        brains = 0

        #INSERT CODE HERE
        while diceRollResults is not None:
            #three shotguns rolled leads to zombiedice.rolls
            #returning None
            brains += diceRollResults['brains']
            if brains <= 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class My_StopAfterTwoShotguns:
    def __init__(self, name):

        self.name = name

    def turn(self, gameState):


        diceRollResults = zombiedice.roll()

        brains = 0
        shotguns = 0
        #INSERT CODE HERE
        while diceRollResults is not None:
            #three shotguns rolled leads to zombiedice.rolls
            #returning None
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

class My_RandomStart:
    def __init__(self, name):

        self.name = name

    def turn(self, gameState):


        diceRollResults = zombiedice.roll()

        brains = 0
        shotguns = 0
        potential_number_of_rolls = [1, 2, 3, 4]
        number_of_rolls_planned = random.choice(potential_number_of_rolls)
        #INSERT CODE HERE
        i = 1
        while diceRollResults is not None:

            #three shotguns rolled leads to zombiedice.rolls
            #returning None
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if i <= number_of_rolls_planned and shotguns <= 2:
                diceRollResults = zombiedice.roll()
                i += 1
            else:
                break

class My_StopAfterShotgunsGreaterBrains:
    def __init__(self, name):

        self.name = name

    def turn(self, gameState):


        diceRollResults = zombiedice.roll()

        brains = 0
        shotguns = 0

        #INSERT CODE HERE

        while diceRollResults is not None:

            #three shotguns rolled leads to zombiedice.rolls
            #returning None
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if shotguns > brains:
                break
            else:
                diceRollResults = zombiedice.roll()


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    My_StopAfterTwoBrains(name = 'My_StopAfterTwoBrains'), My_randomChoiceZombie(name = 'My_randomChoiceZombie'),
    My_StopAfterTwoShotguns(name = 'My_StopAfterTwoShotguns'),
    My_RandomStart(name = 'My_RandomStart'),
    My_StopAfterShotgunsGreaterBrains(name='My_StopAfterShotgunsGreaterBrains')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
