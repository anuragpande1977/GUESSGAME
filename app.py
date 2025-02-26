import streamlit as st
import random
import requests

# Function to get a random word and definition
def get_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if response.status_code == 200:
        word = response.json()[0]
        definition_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if definition_response.status_code == 200:
            definition = definition_response.json()[0]['meanings'][0]['definitions'][0]['definition']
        else:
            definition = "Definition not available."
        return word, definition
    else:
        return "streamlit", "A web app framework for Python."

# Select a random word
word, hint = get_random_word()
shuffled_word = ''.join(random.sample(word, len(word)))

# Streamlit app title
st.title("Word Guessing Game")

# Display hint and shuffled word
st.write(f"**Hint:** {hint}")
st.write(f"**Scrambled Word:** {shuffled_word}")

# User input
user_guess = st.text_input("Enter your guess:")

# Check the guess
if user_guess:
    if user_guess.lower() == word:
        st.success("🎉 Correct! You guessed the word!")
    else:
        st.error("❌ Wrong guess! Try again.")
