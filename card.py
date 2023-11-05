import numpy as np
import random
import math


class Card:
    '''Card Class'''

    def create_bingo_card(num_cards=1, row=5, col=5, start=1, end=75, free=1):
        '''This function is use to generate n numbers of cards'''
        
        cards = []
        num_list = [i for i in range(start, end+1)] # generate numbers based on start and end
        
        slice_num = math.floor(len(num_list)/row) 

        # Generate n num of cards (Dynamic)
        for _ in range(num_cards):
            card = []
            
            # Generate row based on req (Dynamic)
            for i in range(row):
                card.append(random.sample(num_list[i*slice_num:(i+1)*slice_num], col)) # i.e num_cards[1*16:(1+1)*16]
                
            cards.append(np.array(card))

        # Traditional Bingo free position
        if (free == 1 and row == col and row == 5 and col == 5):
            for card in cards:
                card[2][2] = 0

        # Free positions generator (Dynamic)
        free_pos = []

        if (free > 1):
            # Generate random free position co-ordinates
            for i in range(free):
                free_pos_coord = {"x": 0, "y": 0}
                free_pos_coord["x"] = random.randint(0, row-1)
                free_pos_coord["y"] = random.randint(0, col-1)
                free_pos.append(free_pos_coord)
            
            # Insert 0 in all the co-ordinates in free_pos list
            for card in cards:
                for i in range(free):
                    card[free_pos[i]["x"]][free_pos[i]["y"]] = 0 
                    

        # Return only one card if no. cards is 1 else return arr of card (Dynamic)
        if (num_cards == 1):
            return cards[0]
        elif (num_cards > 1):
            return cards
        elif (num_cards < 0):
            return 0

