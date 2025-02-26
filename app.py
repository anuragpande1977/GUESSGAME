import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt

# Sample words and their positions for crossword
words = {
    "apple": [(0, 0, "right")],
    "banana": [(2, 1, "down")],
    "cherry": [(4, 2, "right")],
    "date": [(1, 4, "down")],
    "grape": [(3, 3, "right")]
}

grid_size = 10
crossword_grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Place words in the grid
def place_words():
    for word, positions in words.items():
        for x, y, direction in positions:
            if direction == "right":
                for i, letter in enumerate(word):
                    crossword_grid[y][x + i] = letter
            elif direction == "down":
                for i, letter in enumerate(word):
                    crossword_grid[y + i][x] = letter

place_words()

# Initialize session state for tracking progress
if 'guesses' not in st.session_state:
    st.session_state.guesses = {}

st.title("Crossword Puzzle")

def draw_crossword(grid, guesses):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks(np.arange(grid_size+1)-0.5, minor=True)
    ax.set_yticks(np.arange(grid_size+1)-0.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
    
    for y in range(grid_size):
        for x in range(grid_size):
            char = grid[y][x]
            if char != ' ' and (x, y) in guesses:
                ax.text(x, grid_size-1-y, char, ha='center', va='center', fontsize=12, fontweight='bold')
            else:
                ax.text(x, grid_size-1-y, "_", ha='center', va='center', fontsize=12, fontweight='bold')
    
    st.pyplot(fig)

draw_crossword(crossword_grid, st.session_state.guesses)

# User input
user_word = st.text_input("Enter a word:").strip().lower()

# Check the guess
if user_word:
    if user_word in words:
        st.success(f"🎉 Correct! '{user_word}' is in the crossword!")
        for x, y, direction in words[user_word]:
            if direction == "right":
                for i, letter in enumerate(user_word):
                    st.session_state.guesses[(x + i, y)] = letter
            elif direction == "down":
                for i, letter in enumerate(user_word):
                    st.session_state.guesses[(x, y + i)] = letter
    else:
        st.error("❌ Incorrect! Try another word.")

# Button to restart the game
if st.button("Restart Puzzle"):
    st.session_state.guesses = {}
    st.experimental_rerun()


