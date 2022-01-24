from asyncio import FastChildWatcher
import random

class Piece:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        taken = False

    def display_piece(self):
        print( "|",self.left,"|",self.right,"|\t")

class Board:
    def __init__(self):
        self.pieces = self.set_pieces()

    def set_pieces(self):
        tab = []
        n = 1
        for i in range(7):
            for j in range(n):
                tab.append(Piece(i,j))
            n += 1
        random.shuffle(tab)
        return tab

    def get_pieces(self):
        return self.pieces

    def display_board(self):
        print("board")
        for piece in self.pieces:
            piece.display_piece()
        print("fin board")
class Fil:
    def __init__(self,board):
        self.pieces = board.get_pieces()

    def delete_piece_fil(self):
        self.pieces.pop(0)
    
    def display_fil(self):
        print("Fill")
        for piece in self.pieces:
            piece.display_piece()
        print("fin Fill")

class Terre:
    def __init__(self):
        self.pieces = []
# non tester
    def add_to_terre_from_hand(self,piece,left,inverse):
        if inverse:
            piece.left,piece.right = piece.right,piece.left
        self.pieces.insert(0,piece) if left else self.pieces.append(piece)
# non tester 
    def display_terre(self):
        print("Terre")
        for piece in self.pieces:
            piece.display_piece()
        print("fin Terre")

class Hand:
    def __init__(self,board,nb):
        self.pieces  = self.set_pieces(board,nb) 


    def set_pieces(self,board,nb):
        tab = []
        for i in range(nb):
            tab.append(board.pieces[0])
            board.pieces.pop(0)
        return tab

    def add_to_hand_from_fil(self,fil):
        if len(fil.pieces) > 0:
            self.pieces.append(fil.pieces[0])
            fil.delete_piece_fil()
        else:
            print("fil terminer")
# non tester
    def possibilty_hand(self,terre):
        pos = []
        if len (terre.pieces) == 0:
            pos = self.pieces
        else:
            for piece in self.pieces:
                if piece.left == terre.pieces[0].left or piece.left == terre.pieces[len(terre.pieces)-1].right or piece.right == terre.pieces[0].left or piece.right == terre.pieces[len(terre.pieces)-1].right:
                    pos.append(piece)
        return pos
# non tester verifier si index est dans pos
    def add_to_terre_from_hand(self,terre,pos,index):
        if len(terre.pieces) == 0:
            left = True
            inverse = False
        else:
            if terre.pieces[0].left == pos[index].right:
                inverse =False
                left = True
            if terre.pieces[0].left == pos[index].left:
                inverse = True
                left = True
            if terre.pieces[len(terre.pieces)-1].right == pos[index].right:
                inverse = True
                left = False
            if terre.pieces[len(terre.pieces)-1].right == pos[index].left:
                inverse = False
                left = False

        terre.add_to_terre_from_hand(self.pieces[index],left,inverse)
        self.pieces.pop(index)
        
    def display_poss_hand(self,tab):
        print("possi")
        for piece in tab:
            piece.display_piece()
        print("fin possi")

    def display_hand(self):
        print("hand")
        for piece in self.pieces:
            piece.display_piece()
        print("fin hand")

