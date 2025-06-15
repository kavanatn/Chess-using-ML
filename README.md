# ♟️ Chess Using ML

A web-based chess application that uses Machine Learning to predict and play chess moves. Built with Streamlit and powered by a trained neural network model.

---

## 🚀 Features

- Interactive Chess Board: Visual chess board with piece movement  
- ML-Powered Opponent: ML opponent that uses a trained neural network to make moves  
- Automatic Play: ML automatically responds after each user move  
- Multiple Input Methods:  
  - Click on move buttons to select your move  
  - Enter moves using UCI notation (e.g., e2e4)  
- Game Controls: Undo moves, reset game, view move history  
- Real-time Game Status: Shows current turn, check/checkmate status  
- Move History: Track all moves made during the game  

---

## 🛠️ Technology Stack

- Frontend: Streamlit  
- Chess Logic: `python-chess` library  
- ML Framework: TensorFlow/Keras  
- Board Encoding: One-hot encoding for neural network input  
- Visualization: SVG-based chess board rendering  

---

## 📋 Requirements

```bash
streamlit  
chess  
numpy  
tensorflow  
keras  
pandas  
matplotlib
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/chess-using-ml.git
cd chess-using-ml
```

Ensure you have the trained model:

- Make sure `chess_model.h5` is in the project directory  
- This file contains the trained neural network weights  
- Or train it yourself using the provided Google Colab notebook (see below)

Run the application:

```bash
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

Start playing chess using machine learning!

---

## 🎮 How to Play

- You play as White (first move)  
- Make your move by either:  
  - Clicking on the move buttons displayed  
  - Entering UCI notation in the text input (e.g., "e2e4")  
- ML responds automatically as Black after your move  
- Continue playing until checkmate, stalemate, or draw  

---

## 🧠 ML Model Details

The chess engine uses a neural network that:

- **Input**: One-hot encoded chess board positions (8x8x13 tensor)  
- **Output**: Move evaluation scores  
- **Training**: Trained on chess game data to evaluate board positions  
- **Move Selection**: Chooses moves based on position evaluation  

**Board Encoding:**
- Each square encoded as a 13-dimensional one-hot vector  
- Represents 12 piece types (6 white + 6 black) + empty square  
- Board converted to 8x8x13 tensor for neural network input  

---

## 📓 Model Training

Model training is done using Google Colab. The notebook is available here:

- [`train_and_play.ipynb`](./train_and_play.ipynb)  
- Requires data files located in the `data/` folder:
  - `data/train.csv`
  - `data/test.csv`
- After training, `chess_model.h5` will be generated and used by the Streamlit app

To run the notebook in Google Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/Chess-using-ML/blob/main/train_and_play.ipynb)

---

## 📁 Project Structure

```
chess-using-ml/
├── app.py                # Main Streamlit application  
├── chess_utils.py        # Chess utility functions and ML model interface  
├── chess_model.h5        # Trained neural network model  
├── requirements.txt      # Python dependencies  
├── train_and_play.ipynb  # Google Colab notebook (training)  
├── data/                 # Training and testing data  
│   ├── train.csv  
│   └── test.csv  
└── README.md             # Project documentation  
```

---

## 🎯 Key Functions

- `encode_board()`: Converts chess board to neural network input format  
- `one_hot_encode_piece()`: Encodes individual pieces as one-hot vectors  
- `play_nn()`: Uses ML model to select best move for given position  
- `make_ai_move()`: Handles automatic ML move execution  

---

Enjoy playing chess using machine learning! ♟️🧠
