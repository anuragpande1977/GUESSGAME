import streamlit as st
import chess
import chess.svg
import chess.engine
import os
import base64

# Load Stockfish engine (Update this path based on your OS)
STOCKFISH_PATH = "/usr/local/bin/stockfish"  # Update this path if needed
if not os.path.exists(STOCKFISH_PATH):
    st.error("Stockfish engine not found! Install and update the path.")
    st.stop()

# Initialize chess board
if "board" not in st.session_state:
    st.session_state.board = chess.Board()
    st.session_state.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    st.session_state.game_over = False

# Convert board to an SVG image
def render_board(board):
    board_svg = chess.svg.board(board=board)
    encoded_svg = base64.b64encode(board_svg.encode("utf-8")).decode("utf-8")
    return f'<img src="data:image/svg+xml;base64,{encoded_svg}" width="400"/>'

# Function to handle player move
def player_move(move):
    if move in [m.uci() for m in st.session_state.board.legal_moves]:
        st.session_state.board.push_uci(move)
        return True
    return False

# Function for AI move
def ai_move():
    if not st.session_state.board.is_game_over():
        result = st.session_state.engine.play(st.session_state.board, chess.engine.Limit(time=1.0))
        st.session_state.board.push(result.move)

# Streamlit UI
st.title("♟️ AI Chess Game on Streamlit")

# Display the chess board
st.markdown(render_board(st.session_state.board), unsafe_allow_html=True)

# Move input from player
player_input = st.text_input("Enter your move (e.g., e2e4):", key="move_input")
if st.button("Submit Move"):
    if player_move(player_input):
        if not st.session_state.board.is_game_over():
            ai_move()
    else:
        st.warning("Invalid move! Try again.")

# Display game status
if st.session_state.board.is_checkmate():
    st.session_state.game_over = True
    st.success("Checkmate! The game is over.")
elif st.session_state.board.is_stalemate():
    st.session_state.game_over = True
    st.warning("Stalemate! The game is drawn.")
elif st.session_state.board.is_insufficient_material():
    st.session_state.game_over = True
    st.info("Draw! Insufficient material.")

# Reset game button
if st.button("Restart Game"):
    st.session_state.board = chess.Board()
    st.session_state.game_over = False

# Close Stockfish engine
st.session_state.engine.close()



