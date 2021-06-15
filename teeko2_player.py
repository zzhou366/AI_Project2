
import random
import copy



class Teeko2Player:
    """ An object representation for an AI game player for the game Teeko2.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a Teeko2Player object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    
    

    
    def succ(self, state, marker):
        drop_phase = self.Isdrop(state)
        succ = []

        if drop_phase:
            for i in range(5):
                for j in range(5):
                    if state[i][j] != ' ':
                        continue
                    else:
                        
                        copystate = copy.deepcopy(state)
                        copystate[i][j] = marker
                        succ.append(copystate)
        else:
            for i in range(5):
                for j in range(5):
                    if state[i][j] == marker:
                        # down
                        temp = copy.deepcopy(state)
                        if 0 < i + 1 < 5:
                            if temp[i + 1][j] == ' ':
                                temp[i][j] = ' '
                                temp[i + 1][j] = marker
                                succ.append(temp)
                        # up
                        temp = copy.deepcopy(state)
                        if 5 > i - 1 >= 0:
                            if temp[i - 1][j] == ' ':
                                temp[i][j] = ' '
                                temp[i - 1][j] = marker
                                succ.append(temp)
                        # right
                        temp = copy.deepcopy(state)
                        if 0 < j + 1 < 5:
                            if temp[i][j + 1] == ' ':
                                temp[i][j] = ' '
                                temp[i][j + 1] = marker
                                succ.append(temp)
                        # left
                        temp = copy.deepcopy(state)
                        if 5 > j - 1 >= 0:
                            if temp[i][j - 1] == ' ':
                                temp[i][j] = ' '
                                temp[i][j - 1] = marker
                                succ.append(temp)
                        # downleft
                        temp = copy.deepcopy(state)
                        if 0 < i + 1 < 5:
                            if j - 1 >= 0:
                                if temp[i + 1][j - 1] == ' ':
                                    temp[i][j] = ' '
                                    temp[i + 1][j - 1] = marker
                                    succ.append(temp)
                        # downright
                        temp = copy.deepcopy(state)
                        if 0 < i + 1 < 5:
                            if j + 1 < 5:
                                if temp[i + 1][j + 1] == ' ':
                                    temp[i][j] = ' '
                                    temp[i + 1][j + 1] = marker
                                    succ.append(temp)
                        # upleft
                        temp = copy.deepcopy(state)
                        if 5 > i - 1 >= 0: 
                            if j - 1 >= 0:
                                if temp[i - 1][j - 1] == ' ':
                                    
                                    temp[i][j] = ' '
                                    temp[i - 1][j - 1] = marker
                                    succ.append(temp)
                        # upright
                        temp = copy.deepcopy(state)
                        if 5 > i - 1 >= 0:
                            if j + 1 < 5:
                                if temp[i - 1][j + 1] == ' ':
                                    temp[i][j] = ' '
                                    temp[i - 1][j + 1] = marker
                                    succ.append(temp)

        return succ

    def h_horizon(self, state, marker):
        max = 0
        for row in range(5):
            col = 0
            streak = 0
            while col < 5:
                if state[row][col] == marker:
                    streak += 1
                    col += 1
                else:
                    col += 1
                    if streak > max:
                        max = streak
                        streak = 0
                    else:
                        streak = 0
                   
        return max / 4

    def h_vertical(self, state, marker):
        max = 0
        streak = 0
        for col in range(5):
            row = 0
            while row < 5:
                if state[row][col] == marker:
                    streak += 1
                    row += 1
                else:
                    row += 1
                    if streak > max:
                        max = streak
                        streak = 0
                    else: 
                        streak = 0
        return max / 4

    def h_down_right(self, state, marker):
        max = 0
        #1:
        r1 = 3
        c1 = 0
        streak1 = 0
        while c1 < 4:
            if state[r1][c1] == marker:
                streak1 += 1
                c1 += 1
            else:
                c1 += 1
                if streak1 > max:
                    max = streak1
                    streak1 = 0
                else:
                    streak1 = 0
        #2:
        r2 = 4
        c2 = 0
        streak2 = 0
        while c2 < 5:
            if state[r2][c2] == marker:
                streak2 += 1
                c2 += 1
            else:
                c2 += 1
                if streak2 > max:
                    max = streak2
                    streak2 = 0                
                else:
                    streak2 = 0
        #3:
        r3 = 4
        c3 = 1
        streak3 = 0
        while c3 < 5:
            if state[r3][c3] == marker:
                streak3 += 1
                c3 += 1
            else:
                c3 += 1
                if streak3 > max:
                    max = streak3
                    streak3 = 0
                else:
                    streak3 = 0        
        return max / 4
    

    def h_up_left(self, state, marker):
        max = 0
        #1:
        r1 = 1
        c1 = 0
        streak1 = 0
        while (r1 < 5) and (c1 < 4):
            if state[r1][c1] == marker:
                streak1 += 1
                r1 += 1
                c1 += 1
            else:
                r1 += 1
                c1 += 1
                if streak1 > max:
                    max = streak1
                    streak1 = 0
                else:
                    streak1 = 0
        
        #2:
        r2 = 0
        c2 = 0
        streak2 = 0
        while (r2 < 5) and (c2 < 5):
            if state[r2][c2] == marker:
                streak2 += 1
                r2 += 1
                c2 += 1
            else:
                r2 += 1
                c2 += 1
                if streak2 > max:
                    max = streak2
                    streak2 = 0
                else:
                    streak2 = 0
        
        #3:
        r3 = 0
        c3 = 1
        streak3 = 0
        while (r3 < 5) and (c3 < 5):
            if state[r3][c3] == marker:
                streak3 += 1
                r3 += 1
                c3 += 1
            else:
                r3 += 1
                c3 += 1
                if streak3 > max:
                    max = streak3
                    streak3 = 0
                else:
                    streak3 = 0
        
            
        return max / 4

     
    
    def h_diamond(self, state, marker):
        max = 0
        count = 0
        for i in range(5 - 2):
            for j in range(1, 5 - 1):
                if state[i][j] == marker:
                    count = count + 1
                if state[i + 1][j + 1] == marker:
                    count = count + 1
                if state[i + 2][j] == marker:
                    count = count + 1
                if state[i + 1][j - 1] == marker:
                    count = count + 1
                if max < count:
                    max = count
                count = 0
        return max / 4

    
    def heuristic_game_value(self, state):
        
        terminal = self.game_value(state)
        if terminal == 1:
            return terminal, state
        if terminal == -1:
            return terminal, state

        my = []
        opp = []

        my.append(self.h_horizon(state, self.my_piece))
        my.append(self.h_vertical(state, self.my_piece))
        my.append(self.h_up_left(state, self.my_piece))
        my.append(self.h_down_right(state, self.my_piece))
        my.append(self.h_diamond(state, self.my_piece))
        opp.append(self.h_horizon(state, self.opp))
        opp.append(self.h_vertical(state, self.opp))
        opp.append(self.h_up_left(state, self.opp))
        opp.append(self.h_down_right(state, self.opp))
        opp.append(self.h_diamond(state, self.opp))

        max_h = max(my)
        min_h = max(opp)

        return max_h + (-1) * min_h, state

    # Find the max heuristic value in the given depth, which is 2 here
    # Return if it is a terminal state
    def Max_Value(self, state, depth):
        copymax = copy.deepcopy(state)
        t = self.game_value(state) 
        if t!= 0:
            return t, state

        if depth > 2:
            return self.heuristic_game_value(state)

        else:
            a = float('-Inf')
            for s in self.succ(state, self.my_piece):
                if self.game_value(s) != 0:
                    return self.game_value(s), s
                val, curr = self.Min_Value(s, depth + 1)
                if val > a:
                    a = val
                    copymax = s
        return a, copymax

    # Find the min heuristic value in the given depth, which is 2 here
    # Return if it is a terminal state
    def Min_Value(self, state, depth):
        copystate = copy.deepcopy(state)
        if self.game_value(state) != 0:
            return self.game_value(state), state

        if depth > 2:
            return self.heuristic_game_value(state)

        else:
            b = float('Inf')
            for s in self.succ(state, self.opp):
                if self.game_value(s) != 0:
                    return self.game_value(s), s
                val, curr = self.Max_Value(s, depth + 1)
                if val < b:
                    b = val
                    copystate = s
        return b, copystate



    # Helper methods to find different position in two states
    def findP(self, state, next):
        pos = []
        for i in range(5):
            for j in range(5):
                if state[i][j] != next[i][j]:
                    dif = [i, j]
                    pos.append(dif)
        return pos
    
    def Isdrop(self, state):
        count = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if (state[i][j] == 'r' or state[i][j] == 'b'):
                    count = count + 1
        if (count >= 8):
            return False
        else:
            return True



    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.

        Args:
            state (list of lists): should be the current state of the game as saved in
                this Teeko2Player object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.

                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).

        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """

        drop_phase = self.Isdrop(state)  # detect drop phase

        if not drop_phase:
            #  choose a piece to move and remove it from the board
            # (You may move this condition anywhere, just be sure to handle it)
            #
            # Until this part is implemented and the move list is updated
            # accordingly, the AI will not follow the rules after the drop phase!
            move = []
            a, next = self.Max_Value(state, 0)
            pos = self.findP(state, next)
            # find previous pos
            if state[pos[0][0]][pos[0][1]] == ' ':
                (pre_row, pre_col) = (pos[1][0], pos[1][1])
                (row, col) = (pos[0][0], pos[0][1])
            else:
                (pre_row, pre_col) = (pos[0][0], pos[0][1])
                (row, col) = (pos[1][0], pos[1][1])
            move.insert(0, (row, col))
            move.insert(1, (pre_row, pre_col))
            return move

        #  implement a minimax algorithm to play better
        move = []
        a, next = self.Max_Value(state, 0)
        pos = self.findP(state, next)
        (row, col) = (pos[0][0], pos[0][1])
        while not state[row][col] == ' ':
            (row, col) = (pos[0][0], pos[0][1])

        # ensure the destination (row,col) tuple is at the beginning of the move list
        move.insert(0, (row, col))
        return move

    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row) + ": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this Teeko2Player object, or a generated successor state.

        Returns:
            int: 1 if this Teeko2Player wins, -1 if the opponent wins, 0 if no winner

        TODO: complete checks for diagonal and diamond wins
        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                    return 1 if row[i] == self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i + 1][col] == state[i + 2][col] == state[i + 3][
                    col]:
                    return 1 if state[i][col] == self.my_piece else -1

        # TODO: check \ diagonal wins
        for row in range(2):
            for i in range(2):
                if state[row][i] != ' ' and state[row][i] == state[row + 1][i + 1] == state[row + 2][i + 2] == \
                        state[row + 3][i + 3]:
                    return 1 if state[row][i] == self.my_piece else -1

        # TODO: check / diagonal wins
        for row in range(3, 5):
            for i in range(2):
                if state[row][i] != ' ' and state[row][i] == state[row - 1][i + 1] == state[row - 2][i + 2] == \
                        state[row - 3][i + 3]:
                    return 1 if state[row][i] == self.my_piece else -1

        # TODO: check diamond wins
        for row in range(1, 4):
            for i in range(3):
                if state[row][i] != ' ' and state[row][i] == state[row - 1][i + 1] == state[row][i + 2] == \
                        state[row + 1][i + 1] and state[row][i + 1] == ' ':
                    return 1 if state[row][i] == self.my_piece else -1

        return 0  # no winner yet


############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################





def main():
    print('Hello, this is Samaritan')
    ai = Teeko2Player()
    piece_count = 0
    turn = 0

    # drop phase
    while piece_count < 8 and ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece + " moved at " + chr(move[0][1] + ord("A")) + str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp + "'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0]) - ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece + " moved from " + chr(move[1][1] + ord("A")) + str(move[1][0]))
            print("  to " + chr(move[0][1] + ord("A")) + str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp + "'s turn")
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0]) - ord("A")),
                                      (int(move_from[1]), ord(move_from[0]) - ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        print("AI wins! Game over.")
    else:
        print("You win! Game over.")

    


if __name__ == "__main__":
    main()

# ITSME