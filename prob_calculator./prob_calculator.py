import random
import copy

class Hat:
    
    def __init__(self, **args): # The ** allows for sending multiple keywords
        
        '''        
        For testing...        
        for k, v in args.items():
            for i in range(v):
                print(k)
        '''
        
        # Final one-liner
        
        self.contents = [k for k,v in args.items() for i in range(v)]
    
    def draw(self, nDraw):
        
        return [self.contents.pop(random.randint(0,len(self.contents)-1)) for x in range(nDraw)] if nDraw < len(self.contents) else self.contents
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = 0
    
    for i in range(num_experiments):
        
        # Using deepcopy method to avoid changing the original object
        
        ex_copy = copy.deepcopy(expected_balls)
        
        # Getting a copy of the dict to calculate probability later
        
        hat_copy = copy.deepcopy(hat)
        
        # Making the draw from the hat for this loop
        
        colors = hat_copy.draw(num_balls_drawn)

        # Extracting the balls that were drawn in this loop
        
        for color in colors:
            if color in ex_copy:
                ex_copy[color] -= 1

        # Validating if ALL of the balls that were expected were drawn in this loop, doesn't matter if the drawn balls were higher than expected

        count += 1 if all(vars <= 0 for vars in ex_copy.values()) else 0
    
    # Getting and returning the probability of the expected balls to be drawn

    return count / num_experiments