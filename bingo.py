from card import Card

class Bingo:
    '''Bingo class'''
    
    def check_bingo(matrix):
        '''Check Bingo in the give matrix\n\nReturn values of vert, hor, diag'''
        
        # Initialize counts
        horizontal_count = 0
        vertical_count = 0
        diagonal_count = 0

        # Check horizontal lines
        for row in matrix:
            for i in range(len(row) - 4):
                if all(cell == -1 for cell in row[i:i+5]):
                    horizontal_count += 1

        # Check vertical lines
        for col in range(len(matrix[0])):
            for i in range(len(matrix) - 4):
                if all(matrix[i+j][col] == -1 for j in range(5)):
                    vertical_count += 1

        # Check diagonal lines (from top-left to bottom-right)
        for i in range(len(matrix) - 4):
            for j in range(len(matrix[0]) - 4):
                if all(matrix[i+k][j+k] == -1 for k in range(5)):
                    diagonal_count += 1

        # Check diagonal lines (from top-right to bottom-left)
        for i in range(len(matrix) - 4):
            for j in range(4, len(matrix[0])):
                if all(matrix[i+k][j-k] == -1 for k in range(5)):
                    diagonal_count += 1

        return vertical_count, horizontal_count, diagonal_count                
