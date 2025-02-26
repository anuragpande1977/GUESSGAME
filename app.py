import streamlit as st
import openai
import random

# Set OpenAI API Key (replace with your own API key)
OPENAI_API_KEY = "your-api-key"
openai.api_key = OPENAI_API_KEY

# Initialize session state
if "game_state" not in st.session_state:
    st.session_state.game_state = "start"
    st.session_state.story = ""
    st.session_state.inventory = []
    st.session_state.character = ""

# Function to generate AI response
def generate_story(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI Dungeon Master guiding a player through an adventure. Respond concisely."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

# Game Introduction
st.title("🕵️ AI Dungeon: The Forgotten Realm")
st.write("Welcome, adventurer! Choose your path and shape your own story.")

# Character Selection
if st.session_state.game_state == "start":
    st.write("### Choose your character:")
    character = st.radio("", ["Warrior 🗡️", "Mage 🔥", "Rogue 🏹"])
    if st.button("Start Adventure"):
        st.session_state.character = character
        intro_prompt = f"You are a {character.lower()} in a mysterious dungeon. Describe the scene and what happens next."
        st.session_state.story = generate_story(intro_prompt)
        st.session_state.game_state = "playing"
        st.experimental_rerun()

# Game Loop
elif st.session_state.game_state == "playing":
    st.write("### Your Adventure So Far:")
    st.write(st.session_state.story)

    # User Input
    user_action = st.text_input("What will you do next? (e.g., 'Search the chest', 'Attack the monster')")
    if st.button("Submit Action") and user_action:
        action_prompt = f"The player decides to {user_action}. Continue the story and describe the outcome."
        new_story = generate_story(action_prompt)
        st.session_state.story += "\n\n" + new_story
        st.experimental_rerun()

# Restart Option
if st.session_state.game_state != "start" and st.button("Restart Game"):
    st.session_state.game_state = "start"
    st.session_state.story = ""
    st.session_state.inventory = []
    st.session_state.character = ""
    st.experimental_rerun()


