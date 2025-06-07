import chess
import numpy as np


def one_hot_encode_piece(piece):
    pieces = list('rnbqkpRNBQKP.')
    arr = np.zeros(len(pieces))
    piece_to_index = {p: i for i, p in enumerate(pieces)}
    index = piece_to_index[piece]
    arr[index] = 1
    return arr


def encode_board(board):
    board_str = str(board).replace(' ', '')
    board_list = []
    for row in board_str.split('\n'):
        row_list = [one_hot_encode_piece(piece) for piece in row]
        board_list.append(row_list)
    return np.array(board_list)


def play_nn(fen, model):
    board = chess.Board(fen=fen)
    moves = []
    input_vectors = []
    for move in board.legal_moves:
        candidate_board = board.copy()
        candidate_board.push(move)
        moves.append(move)
        input_vectors.append(encode_board(
            str(candidate_board)).astype(np.int32))

    input_vectors = np.stack(input_vectors)
    scores = model.predict(input_vectors, verbose=0)
    index_of_best_move = np.argmax(
        scores) if board.turn == chess.BLACK else np.argmax(-scores)
    return str(moves[index_of_best_move])
