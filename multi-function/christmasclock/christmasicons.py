
import random 

ORANGE = (255,200,0) 
BLUE = (50,50,255)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,200,0)

TWINKLE_COLOURS = [ORANGE,BLUE,RED,WHITE]

POT_COLOUR = RED 

TWINKLE = (-1,-1,-1) # one of the other colours 


TREE_TEMPLATE = [  [(4,1,GREEN)],
                   [(3,3,GREEN)],
                   [(3,1,TWINKLE),(4,1,GREEN),(5,1,TWINKLE)],
                   [(2,5,GREEN)],
                   [(2,1,TWINKLE),(3,1,GREEN),(4,1,TWINKLE),(5,1,GREEN),(6,1,TWINKLE)],
                   [(1,7,GREEN)],
                   [(1,1,TWINKLE),(2,1,GREEN),(3,1,TWINKLE),(4,1,GREEN),(5,1,TWINKLE),(6,1,GREEN),(7,1,TWINKLE)],
                   [(0,9,GREEN)],
                   [(0,1,TWINKLE),(1,1,GREEN),(2,1,TWINKLE),(3,1,GREEN),(4,1,TWINKLE),(5,1,GREEN),(6,1,TWINKLE),(7,1,GREEN),(8,1,TWINKLE)],
                   [(3,3,POT_COLOUR)],
                   [(3,3,POT_COLOUR)] ]

def get_tree_icon():
    
    tree = []
    
    for line in TREE_TEMPLATE:
        line_vectors = []
        for template_vector in line:
            start,end,colour = template_vector
            if (colour == TWINKLE):
                # replace with random.
                colour = random.choice(TWINKLE_COLOURS)
            line_vectors.append((start,end,colour)) 
            
        tree.append(line_vectors)
        
    return tree 

