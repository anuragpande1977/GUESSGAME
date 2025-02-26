import streamlit as st
import random

# Predefined set of questions and possible answers
questions = [
    ("What is the person's profession?", ["scientist", "actor", "musician", "athlete", "politician"]),
    ("Is the person alive?", ["yes", "no"]),
    ("What is the person's nationality?", ["american", "british", "french", "indian", "japanese"]),
    ("What field is the person famous in?", ["technology", "sports", "movies", "music", "literature"]),
    ("Did the person win any major awards?", ["yes", "no"])
]

# Sample dataset of famous personalities (in a real scenario, expand this dataset)
personalities = {
    ("scientist", "no", "german", "technology", "yes"): "Albert Einstein",
    ("actor", "yes", "american", "movies", "yes"): "Leonardo DiCaprio",
    ("musician", "no", "british", "music", "yes"): "Freddie Mercury",
    ("athlete", "yes", "american", "sports", "yes"): "Serena Williams",
    ("politician", "no", "indian", "politics", "yes"): "Mahatma Gandhi"
}

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

st.title("AI-Powered Personality Guesser")

# Ask questions one by one
if st.session_state.question_index < len(questions):
    question, options = questions[st.session_state.question_index]
    answer = st.radio(question, options, key=f"q{st.session_state.question_index}")
    
    if st.button("Next"):
        st.session_state.answers.append(answer)
        st.session_state.question_index += 1
        st.experimental_rerun()
else:
    # Try to guess the person
    guessed_person = personalities.get(tuple(st.session_state.answers), "I couldn't determine the person!")
    st.write(f"I think the person is: **{guessed_person}**")
    
    if st.button("Play Again"):
        st.session_state.answers = []
        st.session_state.question_index = 0
        st.experimental_rerun()


