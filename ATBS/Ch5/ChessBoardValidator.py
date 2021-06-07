#In this chapter, we used the dictionary value
#{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
#to represent a chess board. Write a function named isValidChessBoard() that
#takes a dictionary argument and returns True or False depending on if the board
# is valid.

#A valid board will have exactly one black king and exactly one white king.
#Each player can only have at most 16 pieces, at most 8 pawns,
#and all pieces must be on a valid space from '1a' to '8h';
#that is, a piece can’t be on space '9z'.
#The piece names begin with either a 'w' or 'b' to represent white or black,
#followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
#This function should detect when a bug has resulted in an improper chess board.


def isValidChessBoard(chessBoard, allowedSpaces):

    # both black and white king must exist
    #if 'wking' not in chessBoard.values() and 'bking' not in chessBoard.values():
    #    isValid = False

    # only one black/white king can exist
    wking = 0
    bking = 0
    for value in chessBoard.values():

        if value == 'wking':
            wking += 1

        elif value == 'bking':
            bking += 1


    if wking != 1 or bking != 1:
        print("Wrong number of Kings!")
        return False

    #Each player can only have at most 16 pieces,
    wpieces = 0
    bpieces = 0
    for value in chessBoard.values():
        if value.find('b') == 0:
            bpieces += 1

        elif value.find('w') == 0:
            wpieces += 1
    if bpieces > 16 or wpieces > 16:
        print("One player has too many pieces!")
        return False


    #at most 8 pawns,
    for piece in chessBoard.values():
        wpawn = 0
        bpawn = 0
        if piece == 'wpawn':
            wpawn +1
        if piece == 'bpawn':
            bpawn +1
        if wpawn > 8 or bpawn > 8:
            print("Too many pawns!")
            return False

    #and all pieces must be on a valid space from '1a' to '8h';
    #that is, a piece can’t be on space '9z'.
    for key in chessBoard.keys():
        if key not in allowedSpaces:
            print("One piece is not on the board!")
            return False

    #The piece names begin with either a 'w' or 'b' to represent white or black,
    #followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
    for value in chessBoard.values():
        if value.find('w') != 0 and value.find('b') != 0:
            print("A piece started with neither w nor b.")
            return False
        if value[1:] not in pieceNames:
            print("One piece is not correctly named!")
            return False

    return True

def validSpaces_generator(list_of_spaces):

    rows = []
    for row in range(1,9):
        number = str(row)
        rows.append(number)

    columns = []
    for numberOfcolumn in range(0,8):
        letter = string.ascii_lowercase[numberOfcolumn]
        columns.append(letter)

    rowcolumn = []
    for i in range(len(rows)):
        for j in range(len(columns)):
            list_of_spaces.append(rows[i]+columns[j])
    return list_of_spaces

##############################################################################
import string
validSpaces_list = []
pieceNames = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
validSpaces_list = validSpaces_generator(validSpaces_list)

#print(validSpaces_list)
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}


isValid = isValidChessBoard(chessBoard, validSpaces_list)
print(isValid)
