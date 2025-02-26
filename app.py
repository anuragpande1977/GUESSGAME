import streamlit as st
import random
import requests

# Function to get a random word and definition
def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        response.raise_for_status()
        word = response.json()[0]
        
        definition_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        definition = "Definition not available."
        
        if definition_response.status_code == 200:
            definition_data = definition_response.json()
            if isinstance(definition_data, list) and definition_data:
                meanings = definition_data[0].get('meanings', [])
                if meanings:
                    definitions = meanings[0].get('definitions', [])
                    if definitions:
                        definition = definitions[0].get('definition', "Definition not available.")
        return word, definition
    except requests.exceptions.RequestException:
        return "streamlit", "A web app framework for Python."

# Initialize session state if not already done
if 'word' not in st.session_state or 'attempts' not in st.session_state:
    st.session_state.word, st.session_state.hint = get_random_word()
    st.session_state.shuffled_word = ''.join(random.sample(st.session_state.word, len(st.session_state.word)))
    st.session_state.attempts = 0

# Streamlit app title
st.title("Word Guessing Game")

# Display hint and shuffled word
st.write(f"**Hint:** {st.session_state.hint}")
st.write(f"**Scrambled Word:** {st.session_state.shuffled_word}")

# User input
user_guess = st.text_input("Enter your guess:")

# Check the guess
if user_guess:
    if user_guess.lower() == st.session_state.word:
        st.success("🎉 Correct! You guessed the word!")
        if st.button("Play Again"):
            st.session_state.word, st.session_state.hint = get_random_word()
            st.session_state.shuffled_word = ''.join(random.sample(st.session_state.word, len(st.session_state.word)))
            st.session_state.attempts = 0
            st.rerun()
    else:
        st.session_state.attempts += 1
        st.error(f"❌ Wrong guess! Attempt {st.session_state.attempts}/3")
        
        if st.session_state.attempts >= 3:
            st.warning(f"The correct word was: {st.session_state.word}")
            if st.button("Try Another Word"):
                st.session_state.word, st.session_state.hint = get_random_word()
                st.session_state.shuffled_word = ''.join(random.sample(st.session_state.word, len(st.session_state.word)))
                st.session_state.attempts = 0
                st.rerun()

