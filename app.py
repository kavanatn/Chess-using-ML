import streamlit as st
import chess
import chess.svg
from keras.models import load_model
from chess_utils import play_nn
import base64
import time


@st.cache_resource
def load_chess_model():
    return load_model("chess_model.h5")


model = load_chess_model()

st.title("♟️ ML Chess Move Generator")

# Initialize board and move history in session state
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()
    st.session_state.history = []  # Store FEN positions for history navigation

# Add current position to history if it's a new move
board = st.session_state.board
if not st.session_state.history or (st.session_state.history and st.session_state.history[-1] != board.fen()):
    st.session_state.history.append(board.fen())


def make_ai_move():

    if not board.is_game_over() and board.turn == chess.BLACK:
        with st.spinner(" thinking..."):
            try:
                best_move_uci = play_nn(board.fen(), model=model)
                move = chess.Move.from_uci(best_move_uci)
                if move in board.legal_moves:
                    piece = board.piece_at(move.from_square)
                    piece_symbol = piece.symbol() if piece else ""
                    move_text = f"{piece_symbol}{chess.square_name(move.from_square)}-{chess.square_name(move.to_square)}"
                    board.push(move)
                    st.session_state.history.append(board.fen())
                    st.success(f"AI: {move_text}")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("suggested illegal move!")
            except Exception as e:
                st.error(f"Error: {e}")


# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Chess Board")

    # Generate SVG of the board
    board_svg = chess.svg.board(
        board=board,
        size=400,
        coordinates=True,
        flipped=False
    )

    # Display the board
    st.image(
        f"data:image/svg+xml;base64,{base64.b64encode(board_svg.encode()).decode()}")

with col2:
    st.subheader("Game Info")

    # Display current player
    current_player = "White" if board.turn else "Black"
    st.write(f"**Current Turn:** {current_player}")

    # Display game status
    if board.is_checkmate():
        winner = "Black" if board.turn else "White"
        st.error(f"Checkmate! {winner} wins!")
    elif board.is_check():
        st.warning("Check!")
    elif board.is_stalemate():
        st.info("Stalemate!")
    elif board.is_game_over():
        st.info("Game Over!")

    # Move counter
    st.write(f"**Move:** {board.fullmove_number}")

    # UCI Notation input
    st.write("**Enter UCI Notation:**")
    user_move = st.text_input("Enter move (e.g., e2e4):", key="uci_input")

    if st.button("Make Move", use_container_width=True):
        if user_move:
            try:
                move = chess.Move.from_uci(user_move.strip())
                if move in board.legal_moves:
                    board.push(move)
                    st.session_state.history.append(board.fen())
                    st.success(f"Your move: {user_move}")
                    st.rerun()
                    # model will move automatically after rerun
                else:
                    st.error("Illegal move!")
            except Exception as e:
                st.error("Invalid move format!")

    st.subheader("Game Controls")

    # Create a more compact button layout
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        if st.button("↩️ Undo", disabled=len(board.move_stack) == 0, use_container_width=True):
            if len(board.move_stack) > 0:
                board.pop()
                if len(st.session_state.history) > 1:
                    st.session_state.history.pop()
                st.success("Undone")
                st.rerun()

    with btn_col2:
        if st.button("🔄 Reset ", use_container_width=True):
            st.session_state.board = chess.Board()
            st.session_state.history = [st.session_state.board.fen()]
            st.rerun()

# Move input section
st.subheader("Make Your Move")

# Create columns for different input methods
move_col1, move_col2 = st.columns([2, 1])

with move_col1:
    st.write("**Click to Select Move:**")

    # Get legal moves and display them as buttons
    legal_moves = list(board.legal_moves)

    if legal_moves and board.turn == chess.WHITE:  # Only show move buttons for human player
        # Group moves by piece type for better organization
        moves_display = []
        for move in legal_moves:
            piece = board.piece_at(move.from_square)
            piece_symbol = piece.symbol() if piece else ""
            move_text = f"{piece_symbol}{chess.square_name(move.from_square)}-{chess.square_name(move.to_square)}"
            if move.promotion:
                move_text += f"={chess.piece_symbol(move.promotion).upper()}"
            moves_display.append((move_text, move.uci()))

        # Display moves in a grid
        cols_per_row = 4
        for i in range(0, len(moves_display), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                if i + j < len(moves_display):
                    move_text, move_uci = moves_display[i + j]
                    if col.button(move_text, key=f"move_{i+j}"):
                        try:
                            move = chess.Move.from_uci(move_uci)
                            if move in board.legal_moves:
                                board.push(move)
                                st.session_state.history.append(board.fen())
                                st.success(f"Your move: {move_text}")
                                st.rerun()
                                # AI will move automatically after rerun
                        except Exception as e:
                            st.error(f"Error making move: {e}")


with move_col2:
    st.write("**Current FEN:**")
    st.text_area("", board.fen(), height=100, label_visibility="collapsed")

# Automatically make AI move if it's AI's turn
if board.turn == chess.BLACK and not board.is_game_over():
    make_ai_move()

# Game history - simplified
if len(board.move_stack) > 0:
    with st.expander("📜 Move History", expanded=False):
        moves_history = []
        temp_board = chess.Board()

        for i, move in enumerate(board.move_stack):
            move_number = (i // 2) + 1
            if i % 2 == 0:  # White move
                piece = temp_board.piece_at(move.from_square)
                piece_symbol = piece.symbol() if piece else ""
                move_text = f"{move_number}. {piece_symbol}{chess.square_name(move.from_square)}-{chess.square_name(move.to_square)}"
            else:  # Black move
                piece = temp_board.piece_at(move.from_square)
                piece_symbol = piece.symbol() if piece else ""
                move_text = f"{piece_symbol}{chess.square_name(move.from_square)}-{chess.square_name(move.to_square)}"

            moves_history.append(move_text)
            temp_board.push(move)

        # Display moves in pairs (White, Black)
        for i in range(0, len(moves_history), 2):
            if i + 1 < len(moves_history):
                st.write(f"{moves_history[i]} {moves_history[i+1]}")
            else:
                st.write(moves_history[i])
