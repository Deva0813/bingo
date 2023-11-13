from card import Card
from bingo import Bingo
import numpy as np
import random
from pdf import PDF_GENERATOR

card = np.array([[12, 9, 2, 11, 10],
        [22, 23, 17, 27, 20],
        [32, 34,  0, 35, 42],
        [56, 54, 55, 57, 48],
        [65, 72, 75, 63, 62]])

numbers = random.sample(range(1,76),75)

for i in range(0,len(card)):
    for j in range(0,len(card[0])):
        if(card[i][j] in numbers):
            card[i][j] = -1

print(card)

bingo = Bingo.check_bingo(card)

print(bingo)
print(sum(bingo))

# Generate pdf
cards = Card.create_bingo_card(num_cards=20)
PDF_GENERATOR.create_bingo_cards_pdf(cards)

