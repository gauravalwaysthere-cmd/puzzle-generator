import random
import string   


words = ('FLOWERS', 'RIVER', 'FOREST', 'CLOUD', 'GARDEN')
grid_size = 15

grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

for word in words:
    row_pos = random.randint(0, grid_size - 1)
    col_pos = random.randint(0, grid_size - len(word))
    for i, letter in enumerate(word):
        grid[row_pos][col_pos + i] = letter
        
   

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == ' ':
            grid[r][c] = random.choice(string.ascii_uppercase)
            

for i, row in enumerate(grid):
    print(f"Row {i}: {' '.join(row)}")
            
print("\nWords to find:")
#for word in words:
    #print(word)         
    #print(f"- {word}")
print ( " ".join(words))

        
