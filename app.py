import streamlit as st
import random

# Define subjects and word banks for random sentence generation
subjects = {
    "Science": ["energy", "photosynthesis", "gravity", "atom", "molecule"],
    "History": ["revolution", "empire", "colonization", "war", "president"],
    "Math": ["equation", "algebra", "geometry", "calculus", "fraction"]
}

# Function to generate a random sentence with a missing word
def generate_sentence(subject):
    word = random.choice(subjects[subject])
    sentence_templates = [
        f"The concept of {word} is fundamental in {subject}.",
        f"One of the most important discoveries in {subject} involves {word}.",
        f"Students often study {word} when learning about {subject}.",
        f"The principle of {word} has shaped modern {subject} theories.",
        f"Understanding {word} is crucial for grasping {subject} concepts."
    ]
    sentence = random.choice(sentence_templates)
    masked_sentence = sentence.replace(word, "___")
    return masked_sentence, word

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'selected_subject' not in st.session_state:
    st.session_state.selected_subject = None
if 'current_sentence' not in st.session_state:
    st.session_state.current_sentence, st.session_state.current_answer = "", ""

st.title("Fill in the Blank Game")

# Ask the user to select a subject
if st.session_state.selected_subject is None:
    st.session_state.selected_subject = st.selectbox("Choose a subject to play:", list(subjects.keys()), key="subject")
    st.session_state.current_sentence, st.session_state.current_answer = generate_sentence(st.session_state.selected_subject)
    st.session_state.score = 0

st.write(f"**Question:** {st.session_state.current_sentence}")
user_answer = st.text_input("Your answer:", key="answer").strip().lower()

if st.button("Submit"):
    if user_answer:
        if user_answer == st.session_state.current_answer.lower():
            st.success("🎉 Correct! You earned 100 points.")
            st.session_state.score += 100
        else:
            st.error(f"❌ Incorrect! The correct answer was: {st.session_state.current_answer}")
        
        # Generate a new question
        st.session_state.current_sentence, st.session_state.current_answer = generate_sentence(st.session_state.selected_subject)
        st.experimental_rerun()

st.write(f"Current Score: {st.session_state.score}")

if st.button("Play Again"):
    st.session_state.selected_subject = None
    st.session_state.current_sentence, st.session_state.current_answer = "", ""
    st.session_state.score = 0
    st.experimental_rerun()


