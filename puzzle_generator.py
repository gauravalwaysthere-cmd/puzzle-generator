import random
import string
import json

def load_word_bank():
    with open('word_bank.json', 'r') as file:
        return json.load(file)

def get_theme_words(theme, word_bank):
    if theme not in word_bank:
        raise ValueError(f"Theme not found. Available themes: {list(word_bank.keys())}")
    return word_bank[theme]

def create_grid(grid_size):
    return [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

def place_words(grid, words, grid_size):
    for word in words:
        placed = False
        attempts = 0
        max_attempts = grid_size * grid_size * 10

        while not placed and attempts < max_attempts:
            attempts += 1
            row_pos = random.randint(0, grid_size - 1)
            col_pos = random.randint(0, grid_size - len(word))
            can_place = True

            for i, letter in enumerate(word):
                existing_letter = grid[row_pos][col_pos + i]
                if existing_letter != ' ' and existing_letter != letter:
                    can_place = False
                    break

            if can_place:
                for i, letter in enumerate(word):
                    grid[row_pos][col_pos + i] = letter
                placed = True

        if not placed:
            print(f"Could not place '{word}' after {max_attempts} attempts.")

def fill_empty_spaces(grid, grid_size):
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == ' ':
                grid[r][c] = random.choice(string.ascii_uppercase)

def verify_words(grid, words, grid_size, debug=False):
    for word in words:
        found = False
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == word[0]:
                    if c + len(word) <= grid_size and all(grid[r][c + i] == word[i] for i in range(len(word))):
                        if debug:
                            print(f"✅ Found '{word}' at (row {r}, col {c})")
                        found = True
                        break
            if found:
                break
        if not found:
            print(f"⚠️ WARNING: '{word}' missing from grid!")

def print_grid(grid, grid_size, theme, words):
    print("\n*** WORD SEARCH PUZZLE ***")
    print(f"    Theme: {theme.upper()}\n")
    print("   " + " ".join(f"{i:2}" for i in range(grid_size)))
    print("   " + "--" * grid_size)
    for i, row in enumerate(grid):
        print(f"{i:2} | {' '.join(row)}")
    print("\n" + "="*30)
    print("WORDS TO FIND:")
    print("="*30)
    for word in words:
        print(f"  - {word}")

if __name__ == "__main__":
    grid_size = 15
    word_bank = load_word_bank()

    theme = input("Enter puzzle theme from: " + " - ".join(word_bank.keys()) + ": ")

    words = get_theme_words(theme, word_bank)
    grid = create_grid(grid_size)
    place_words(grid, words, grid_size)
    fill_empty_spaces(grid, grid_size)
    print_grid(grid, grid_size, theme, words)

    debug = False  # set to True to see word positions
    verify_words(grid, words, grid_size, debug)
