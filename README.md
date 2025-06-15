# ♟️ Chess Using ML

A web-based chess application that uses Machine Learning to predict and play chess moves. Built with Streamlit and powered by a trained neural network model.

## 🚀 Features

- **Interactive Chess Board**: Visual chess board with piece movement
- **ML-Powered Opponent**: AI opponent that uses a trained neural network to make moves
- **Automatic Play**: AI automatically responds after each user move
- **Multiple Input Methods**: 
  - Click on move buttons to select your move
  - Enter moves using UCI notation (e.g., e2e4)
- **Game Controls**: Undo moves, reset game, view move history
- **Real-time Game Status**: Shows current turn, check/checkmate status
- **Move History**: Track all moves made during the game

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Chess Logic**: python-chess library
- **ML Framework**: TensorFlow/Keras
- **Board Encoding**: One-hot encoding for neural network input
- **Visualization**: SVG-based chess board rendering

## 📋 Requirements

```
streamlit
chess
numpy
tensorflow
keras
```

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/chess-using-ml.git
   cd chess-using-ml
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the trained model**
   - Make sure `chess_model.h5` is in the project directory
   - This file contains the trained neural network weights

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Start playing chess against the ML model!

## 🎮 How to Play

1. **You play as White** (first move)
2. **Make your move** by either:
   - Clicking on the move buttons displayed
   - Entering UCI notation in the text input (e.g., "e2e4")
3. **AI responds automatically** as Black after your move
4. **Continue playing** until checkmate, stalemate, or draw

## 🧠 ML Model Details

The chess engine uses a neural network that:
- **Input**: One-hot encoded chess board positions (8x8x13 tensor)
- **Output**: Move evaluation scores
- **Training**: Trained on chess game data to evaluate board positions
- **Move Selection**: Chooses moves based on position evaluation

### Board Encoding
- Each square encoded as 13-dimensional one-hot vector
- Represents 12 piece types (6 white + 6 black) + empty square
- Board converted to 8x8x13 tensor for neural network input

## 📁 Project Structure

```
chess-using-ml/
├── app.py              # Main Streamlit application
├── chess_utils.py      # Chess utility functions and ML model interface
├── chess_model.h5      # Trained neural network model
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🎯 Key Functions

- `encode_board()`: Converts chess board to neural network input format
- `one_hot_encode_piece()`: Encodes individual pieces as one-hot vectors
- `play_nn()`: Uses ML model to select best move for given position
- `make_ai_move()`: Handles automatic AI move execution
---

**Enjoy playing chess against machine learning!** ♟️🤖
```

