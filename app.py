import streamlit as st
import random

# Define subjects and questions
subjects = {
    "Science": [
        ("The sun is a ___ of energy.", "source"),
        ("Plants produce oxygen through ___.", "photosynthesis"),
        ("Water boils at ___ degrees Celsius.", "100")
    ],
    "History": [
        ("The first President of the United States was ___.", "George Washington"),
        ("The Great Wall of China was built to protect against ___.", "invaders"),
        ("World War II ended in ___.", "1945")
    ],
    "Math": [
        ("The square root of 81 is ___.", "9"),
        ("A triangle has ___ sides.", "3"),
        ("The value of pi (π) is approximately ___.", "3.14")
    ]
}

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'selected_subject' not in st.session_state:
    st.session_state.selected_subject = None

st.title("Fill in the Blank Game")

# Ask the user to select a subject
if st.session_state.selected_subject is None:
    st.session_state.selected_subject = st.selectbox("Choose a subject to play:", list(subjects.keys()))
    st.session_state.question_index = 0
    st.session_state.score = 0

subject = st.session_state.selected_subject
questions = subjects[subject]

# Display current question
if st.session_state.question_index < len(questions):
    question, answer = questions[st.session_state.question_index]
    st.write(f"**Question:** {question}")
    user_answer = st.text_input("Your answer:").strip().lower()
    
    if user_answer:
        if user_answer == answer.lower():
            st.success("🎉 Correct! You earned 100 points.")
            st.session_state.score += 100
        else:
            st.error("❌ Incorrect. Try the next question.")
        
        st.session_state.question_index += 1
        st.experimental_rerun()
else:
    st.write(f"Game over! Your final score: {st.session_state.score}")
    if st.button("Play Again"):
        st.session_state.selected_subject = None
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.experimental_rerun()


