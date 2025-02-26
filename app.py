import streamlit as st
import random

# Predefined set of personality-based questions and possible answers
questions = [
    ("Do you prefer the morning or night?", ["morning", "night"]),
    ("Are you more introverted or extroverted?", ["introverted", "extroverted"]),
    ("Do you enjoy creative or analytical tasks more?", ["creative", "analytical"]),
    ("Would you rather spend time alone or in a group?", ["alone", "group"]),
    ("Do you prefer reading books or watching movies?", ["books", "movies"]),
    ("Are you more adventurous or cautious?", ["adventurous", "cautious"]),
    ("Do you like working with technology or people more?", ["technology", "people"]),
    ("Would you rather live in a big city or the countryside?", ["big city", "countryside"])
]

# Sample dataset mapping answer combinations to possible names
name_predictions = {
    ("morning", "introverted", "creative", "alone", "books", "cautious", "technology", "big city"): "Alice",
    ("night", "extroverted", "analytical", "group", "movies", "adventurous", "people", "big city"): "Michael",
    ("morning", "extroverted", "creative", "group", "books", "adventurous", "people", "countryside"): "Sophia",
    ("night", "introverted", "analytical", "alone", "movies", "cautious", "technology", "countryside"): "David"
}

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

st.title("AI-Powered Name Guesser")

# Ask questions one by one
if st.session_state.question_index < len(questions):
    question, options = questions[st.session_state.question_index]
    answer = st.radio(question, options, key=f"q{st.session_state.question_index}")
    
    if st.button("Next"):
        st.session_state.answers.append(answer)
        st.session_state.question_index += 1
        st.experimental_rerun()
else:
    # Try to guess the user's name
    guessed_name = name_predictions.get(tuple(st.session_state.answers), "I couldn't determine your name! But you seem unique!")
    st.write(f"Based on your answers, I think your name could be: **{guessed_name}**")
    
    if st.button("Play Again"):
        st.session_state.answers = []
        st.session_state.question_index = 0
        st.experimental_rerun()


