from board import Board , Hand , Fil , Terre

def main():
    board = Board()
    # board.display_board()
    hand1 = Hand(board,7)
    hand1.display_hand()
    # print(len(board.pieces))
    fil = Fil(board)
    # fil.display_fil()
    terre = Terre()
    terre.display_terre()
    hand1.display_poss_hand(hand1.possibilty_hand(terre))
    hand1.add_to_terre_from_hand(terre,hand1.possibilty_hand(terre),2)
    hand1.display_hand()
    terre.display_terre()
    hand1.display_poss_hand(hand1.possibilty_hand(terre))
    hand1.add_to_terre_from_hand(terre,hand1.possibilty_hand(terre),0)
    hand1.display_hand()
    terre.display_terre()
    # hand1.display_poss_hand(tab)

    # for i in range(len(hand1.pieces)):
    #     if hand1.pieces[i].left == 6 & hand1.pieces[i].right == 6:
    #         print("hand1")

    # for i in range(len(hand2.pieces)):
    #     if hand2.pieces[i].left == 6 & hand2.pieces[i].right == 6:
    #         print("hand2")

    # for i in range(len(fil.pieces)):
    #     if fil.pieces[i].left == 6 & fil.pieces[i].right == 6:
    #         print("fil")hand1.display_hand()

   
if __name__ == '__main__' :
    main()